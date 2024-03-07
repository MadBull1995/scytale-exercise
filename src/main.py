from .data import GithubIntegrationData, GitHubAPI

if __name__ == "__main__":
    org_name = "Scytale-exercise"
    api = GitHubAPI()
    process = GithubIntegrationData(api)
    data = process.ingest(owner=org_name)
    data = process.transform(owner=org_name)
    process.load(data, owner=org_name)