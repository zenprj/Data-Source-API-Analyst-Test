# GitHub API Documentation

## [Search Repositories](https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-repositories)
The `Search repositories` endpoint allows you to find repositories based on various criteria. This method returns up to 100 results per page and supports filters such as query keywords, sorting, and pagination.

You can also retrieve text match metadata for the name and description fields when you pass the text-match media type.

### Example Query
To search for popular Tetris repositories written in assembly code, you can use the following query:

```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/search/repositories?q=Q"
```

## [Commits](https://docs.github.com/en/rest/commits/commits?apiVersion=2022-11-28)

To make a request to the GitHub API to retrieve commits from a specific repository, use the following `curl` command:

```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/commits
```

## [Contents](https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28)

```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/contents/PATH
```