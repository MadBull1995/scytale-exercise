from pyspark.sql import types as T

_USER = T.StructType([
    T.StructField("login", T.StringType(), True),
    T.StructField("id", T.LongType(), True),
    T.StructField("node_id", T.StringType(), True),
    T.StructField("avatar_url", T.StringType(), True),
    T.StructField("gravatar_id", T.StringType(), True),
    T.StructField("url", T.StringType(), True),
    T.StructField("html_url", T.StringType(), True),
    T.StructField("followers_url", T.StringType(), True),
    T.StructField("following_url", T.StringType(), True),
    T.StructField("gists_url", T.StringType(), True),
    T.StructField("starred_url", T.StringType(), True),
    T.StructField("subscriptions_url", T.StringType(), True),
    T.StructField("organizations_url", T.StringType(), True),
    T.StructField("repos_url", T.StringType(), True),
    T.StructField("events_url", T.StringType(), True),
    T.StructField("received_events_url", T.StringType(), True),
    T.StructField("type", T.StringType(), True),
    T.StructField("site_admin", T.BooleanType(), True)
])

REPO = T.StructType([
    T.StructField("id", T.LongType(), True),
    T.StructField("node_id", T.StringType(), True),
    T.StructField("name", T.StringType(), True),
    T.StructField("full_name", T.StringType(), True),
    T.StructField("owner", _USER, True),
    T.StructField("private", T.BooleanType(), True),
    T.StructField("html_url", T.StringType(), True),
    T.StructField("description", T.StringType(), True),
    T.StructField("fork", T.BooleanType(), True),
    T.StructField("url", T.StringType(), True),
    T.StructField("archive_url", T.StringType(), True),
    T.StructField("assignees_url", T.StringType(), True),
    T.StructField("blobs_url", T.StringType(), True),
    T.StructField("branches_url", T.StringType(), True),
    T.StructField("collaborators_url", T.StringType(), True),
    T.StructField("comments_url", T.StringType(), True),
    T.StructField("commits_url", T.StringType(), True),
    T.StructField("compare_url", T.StringType(), True),
    T.StructField("contents_url", T.StringType(), True),
    T.StructField("contributors_url", T.StringType(), True),
    T.StructField("deployments_url", T.StringType(), True),
    T.StructField("downloads_url", T.StringType(), True),
    T.StructField("events_url", T.StringType(), True),
    T.StructField("forks_url", T.StringType(), True),
    T.StructField("git_commits_url", T.StringType(), True),
    T.StructField("git_refs_url", T.StringType(), True),
    T.StructField("git_tags_url", T.StringType(), True),
    T.StructField("git_url", T.StringType(), True),
    T.StructField("issue_comment_url", T.StringType(), True),
    T.StructField("issue_events_url", T.StringType(), True),
    T.StructField("issues_url", T.StringType(), True),
    T.StructField("keys_url", T.StringType(), True),
    T.StructField("labels_url", T.StringType(), True),
    T.StructField("languages_url", T.StringType(), True),
    T.StructField("merges_url", T.StringType(), True),
    T.StructField("milestones_url", T.StringType(), True),
    T.StructField("notifications_url", T.StringType(), True),
    T.StructField("pulls_url", T.StringType(), True),
    T.StructField("releases_url", T.StringType(), True),
    T.StructField("ssh_url", T.StringType(), True),
    T.StructField("stargazers_url", T.StringType(), True),
    T.StructField("statuses_url", T.StringType(), True),
    T.StructField("subscribers_url", T.StringType(), True),
    T.StructField("subscription_url", T.StringType(), True),
    T.StructField("tags_url", T.StringType(), True),
    T.StructField("teams_url", T.StringType(), True),
    T.StructField("trees_url", T.StringType(), True),
    T.StructField("clone_url", T.StringType(), True),
    T.StructField("mirror_url", T.StringType(), True),
    T.StructField("hooks_url", T.StringType(), True),
    T.StructField("svn_url", T.StringType(), True),
    T.StructField("homepage", T.StringType(), True),
    T.StructField("language", T.StringType(), True),
    T.StructField("forks_count", T.LongType(), True),
    T.StructField("stargazers_count", T.LongType(), True),
    T.StructField("watchers_count", T.LongType(), True),
    T.StructField("size", T.LongType(), True),
    T.StructField("default_branch", T.StringType(), True),
    T.StructField("open_issues_count", T.LongType(), True),
    T.StructField("is_template", T.BooleanType(), True),
    T.StructField("topics", T.ArrayType(T.StringType()), True),
    T.StructField("has_issues", T.BooleanType(), True),
    T.StructField("has_projects", T.BooleanType(), True),
    T.StructField("has_wiki", T.BooleanType(), True),
    T.StructField("has_pages", T.BooleanType(), True),
    T.StructField("has_downloads", T.BooleanType(), True),
    T.StructField("archived", T.BooleanType(), True),
    T.StructField("disabled", T.BooleanType(), True),
    T.StructField("visibility", T.StringType(), True),
    T.StructField("pushed_at", T.StringType(), True),
    T.StructField("created_at", T.StringType(), True),
    T.StructField("updated_at", T.StringType(), True),
    T.StructField("permissions", T.StructType([
        T.StructField("admin", T.BooleanType(), True),
        T.StructField("push", T.BooleanType(), True),
        T.StructField("pull", T.BooleanType(), True)
    ]), True),
    T.StructField("allow_rebase_merge", T.BooleanType(), True),
    T.StructField("template_repository", T.NullType(), True),
    T.StructField("temp_clone_token", T.StringType(), True),
    T.StructField("allow_squash_merge", T.BooleanType(), True),
    T.StructField("allow_auto_merge", T.BooleanType(), True),
    T.StructField("delete_branch_on_merge", T.BooleanType(), True),
    T.StructField("allow_merge_commit", T.BooleanType(), True),
    T.StructField("subscribers_count", T.LongType(), True),
    T.StructField("network_count", T.LongType(), True),
    T.StructField("license", T.StructType([
        T.StructField("key", T.StringType(), True),
        T.StructField("name", T.StringType(), True),
        T.StructField("url", T.StringType(), True),
        T.StructField("spdx_id", T.StringType(), True),
        T.StructField("node_id", T.StringType(), True),
        T.StructField("html_url", T.StringType(), True)
    ]), True),
    T.StructField("forks", T.LongType(), True),
    T.StructField("open_issues", T.LongType(), True),
    T.StructField("watchers", T.LongType(), True)
])

PR_SCHEMA = T.StructType([
    T.StructField("url", T.StringType(), True),
    T.StructField("id", T.LongType(), True),
    T.StructField("node_id", T.StringType(), True),
    T.StructField("html_url", T.StringType(), True),
    T.StructField("diff_url", T.StringType(), True),
    T.StructField("patch_url", T.StringType(), True),
    T.StructField("issue_url", T.StringType(), True),
    T.StructField("commits_url", T.StringType(), True),
    T.StructField("review_comments_url", T.StringType(), True),
    T.StructField("review_comment_url", T.StringType(), True),
    T.StructField("comments_url", T.StringType(), True),
    T.StructField("statuses_url", T.StringType(), True),
    T.StructField("number", T.LongType(), True),
    T.StructField("state", T.StringType(), True),
    T.StructField("locked", T.BooleanType(), True),
    T.StructField("title", T.StringType(), True),
    T.StructField("user", _USER, True),
    T.StructField("body", T.StringType(), True),
    T.StructField("labels", T.ArrayType(
        T.StructType([
            T.StructField("id", T.LongType(), True),
            T.StructField("node_id", T.StringType(), True),
            T.StructField("url", T.StringType(), True),
            T.StructField("name", T.StringType(), True),
            T.StructField("description", T.StringType(), True),
            T.StructField("color", T.StringType(), True),
            T.StructField("default", T.BooleanType(), True)
        ])
    ), True),
    T.StructField("milestone", T.StructType([
        T.StructField("url", T.StringType(), True),
        T.StructField("html_url", T.StringType(), True),
        T.StructField("labels_url", T.StringType(), True),
        T.StructField("id", T.LongType(), True),
        T.StructField("node_id", T.StringType(), True),
        T.StructField("number", T.LongType(), True),
        T.StructField("state", T.StringType(), True),
        T.StructField("title", T.StringType(), True),
        T.StructField("description", T.StringType(), True),
        T.StructField("creator", _USER, True),
        T.StructField("open_issues", T.LongType(), True),
        T.StructField("closed_issues", T.LongType(), True),
        T.StructField("created_at", T.StringType(), True),
        T.StructField("updated_at", T.StringType(), True),
        T.StructField("closed_at", T.StringType(), True),
        T.StructField("due_on", T.StringType(), True)
    ]), True),
    T.StructField("active_lock_reason", T.StringType(), True),
    T.StructField("created_at", T.StringType(), True),
    T.StructField("updated_at", T.StringType(), True),
    T.StructField("closed_at", T.StringType(), True),
    T.StructField("merged_at", T.StringType(), True),
    T.StructField("merge_commit_sha", T.StringType(), True),
    T.StructField("assignee", _USER, True),
    T.StructField("assignees", T.ArrayType(
        _USER
    ), True),
    T.StructField("requested_reviewers", T.ArrayType(
        _USER
    ), True),
    T.StructField("requested_teams", T.ArrayType(
        T.StructType([
            T.StructField("id", T.LongType(), True),
            T.StructField("node_id", T.StringType(), True),
            T.StructField("url", T.StringType(), True),
            T.StructField("html_url", T.StringType(), True),
            T.StructField("name", T.StringType(), True),
            T.StructField("slug", T.StringType(), True),
            T.StructField("description", T.StringType(), True),
            T.StructField("privacy", T.StringType(), True),
            T.StructField("permission", T.StringType(), True),
            T.StructField("notification_setting", T.StringType(), True),
            T.StructField("members_url", T.StringType(), True),
            T.StructField("repositories_url", T.StringType(), True),
            T.StructField("parent", T.NullType(), True)
        ])
    ), True),
    T.StructField("head", T.StructType([
        T.StructField("label", T.StringType(), True),
        T.StructField("ref", T.StringType(), True),
        T.StructField("sha", T.StringType(), True),
        T.StructField("user", _USER, True),
        T.StructField("repo", REPO, True)
    ]), True),
    T.StructField("base", T.StructType([
        T.StructField("label", T.StringType(), True),
        T.StructField("ref", T.StringType(), True),
        T.StructField("sha", T.StringType(), True),
        T.StructField("user", _USER, True),
        T.StructField("repo", REPO, True)
    ]), True),
    T.StructField("_links", T.StructType([
        T.StructField("self", T.StructType([
            T.StructField("href", T.StringType(), True)
        ]), True),
        T.StructField("html", T.StructType([
            T.StructField("href", T.StringType(), True)
        ]), True),
        T.StructField("issue", T.StructType([
            T.StructField("href", T.StringType(), True)
        ]), True),
        T.StructField("comments", T.StructType([
            T.StructField("href", T.StringType(), True)
        ]), True),
        T.StructField("review_comments", T.StructType([
            T.StructField("href", T.StringType(), True)
        ]), True),
        T.StructField("review_comment", T.StructType([
            T.StructField("href", T.StringType(), True)
        ]), True),
        T.StructField("commits", T.StructType([
            T.StructField("href", T.StringType(), True)
        ]), True),
        T.StructField("statuses", T.StructType([
            T.StructField("href", T.StringType(), True)
        ]), True)
    ]), True),
    T.StructField("author_association", T.StringType(), True),
    T.StructField("auto_merge", T.NullType(), True),
    T.StructField("draft", T.BooleanType(), True)
])

JSON_SCHEMA = T.StructType([
    T.StructField("repo", REPO, True),
    T.StructField("prs", T.ArrayType(
        PR_SCHEMA
    ), True)
])

PROCESSED_SCHEMA = T.StructType([
    T.StructField("Organization Name", T.StringType(), True),
    T.StructField("repository_id", T.StringType(), True),
    T.StructField("repository_name", T.StringType(), True),
    T.StructField("repository_owner", T.StringType(), True),
    T.StructField("num_prs", T.IntegerType(), True),
    T.StructField("num_prs_merged", T.IntegerType(), True),
    T.StructField("merged_at", T.TimestampType(), True),
    T.StructField("is_compliant", T.BooleanType(), True),
])