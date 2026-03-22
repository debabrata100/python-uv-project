from .api import Api_Service
from .analysis import json_to_csv_excel
import json
import os
from collections import defaultdict

service = Api_Service()


def export_data(filename, data):
    os.makedirs("data/output", exist_ok=True)
    filename = os.path.join("data/output", filename)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_user_profile():
    return service.get_profile()


def get_user_repos(repo_url):
    return service.get_repos(repo_url)


def get_repo_commits(commit_url):
    return service.get_repos(commit_url)


def main():
    profile = get_user_profile()
    if profile:
        export_data("profile.json", profile)
        repos = get_user_repos(profile["repos_url"])
        export_data("repos.json", repos)
        repo_commits = {}
        for repo in repos:
            commit_url = str(repo["commits_url"]).replace("{/sha}", "")
            repo_commits[repo["name"]] = get_repo_commits(commit_url)
        year_wise_commit_count = defaultdict(int)
        for key in repo_commits.keys():
            for commit in repo_commits[key]:
                try:
                    date = commit["commit"]["author"]["date"]
                    if date:
                        year = str(date)[:4]
                        year_wise_commit_count[year] += 1
                except Exception as e:  # noqa: F841
                    continue
        sorted_commits = {}
        for year in sorted(year_wise_commit_count.keys()):
            sorted_commits[year] = year_wise_commit_count[year]
        export_data("commit_count.json", sorted_commits)
        json_to_csv_excel("commit_count.json")


if __name__ == "__main__":
    main()
