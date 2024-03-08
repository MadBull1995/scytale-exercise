from typing import List, Tuple
from pyspark.sql import SparkSession, Row
from pyspark.sql import functions as F

from .api import GitHubAPI
from ._schema import JSON_SCHEMA

SPARK_APP_NAME = "github_pr_etl"

class GithubIntegrationData():

    def __init__(self, github_api: GitHubAPI, output_dir="./data"):
        self.api = github_api
        self.spark = SparkSession.builder.appName(SPARK_APP_NAME).getOrCreate()
        self._setup(output_dir)

    def ingest(self, owner, type="orgs") -> List[Tuple[dict, str]]:
        if owner:
            repos_list = []
            repos = self._list_repos(owner, type=type)
            for repo in repos:
                repo_name = repo['name']
                prs = self._list_pull_requests(owner, repo_name)
                repo_data = {
                    "repo": repo,
                    "prs": prs
                }
                file_name = self._save_as_json(owner, repo_name, repo_data)
                repos_list.append((repo_data, file_name))
            return repos_list
        else:
            raise Exception("'owner' must be specified")

    def transform(self, owner):
        df = (self.spark
                .read
                .schema(JSON_SCHEMA)
                .json(f"{self.base_path}/{owner}/**/*.json"))
        
        df = self._transform_process(df)
        return df

    def load(self, data, owner, output_file_name="output", format="parquet"):
        if format == "parquet":
            (data
                .write
                .mode("overwrite")
                .parquet(f"{self.base_path}/{owner}/{output_file_name}"))
        else:
            raise Exception(f"unimplemented format to save data '{format}'")
        
    def _list_repos(self, name, type="orgs"):
        return self.api.make_request(f"{type}/{name}/repos")
    
    def _list_pull_requests(self, name, repo):
        return self.api.make_paginated_request(f"repos/{name}/{repo}/pulls", params={"state": "all"})
    
    def _save_as_json(self, owner, repo_name, data) -> str:
        file_name = self._format_path(owner, repo_name)
        if data:  # Check if data is not empty
            df = self.spark.createDataFrame([data], JSON_SCHEMA)
            (df
                .repartition(1)
                .write
                .mode("overwrite")
                .json(file_name))
        else:
            df = self.spark.createDataFrame([], JSON_SCHEMA)
            (df
                .repartition(1)
                .write
                .mode("overwrite")
                .json(file_name))
        return file_name

    def _transform_process(self, df):
        # Transform the data
        transformed_df = df.select(
            F.split(F.col("repo.full_name"), "/").getItem(0).alias("Organization Name"),
            F.col("repo.id").cast("string").alias("repository_id"),
            F.col("repo.name").alias("repository_name"),
            F.col("repo.owner.login").alias("repository_owner"),
            F.explode_outer("prs").alias("pr")
        ).groupBy(
            "Organization Name",
            "repository_id",
            "repository_name",
            "repository_owner"
        ).agg(
            F.count("pr.url").alias("num_prs"),
            F.count(F.when(F.col("pr.merged_at").isNotNull(), True)).alias("num_prs_merged"),
            F.max("pr.merged_at").alias("merged_at")
        ).withColumn(
            "is_compliant",
            (F.col("num_prs") == F.col("num_prs_merged")) & F.lower(F.col("repository_owner")).contains("scytale")
        )

        return transformed_df

    def _format_path(self, org_name, repo_name):
        return f"{self.base_path}/{org_name}/{repo_name}"

    def _setup(self, output_dir):
        self.base_path = output_dir