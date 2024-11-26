import requests
import json
import time
from pprint import pprint

#Set up token and headers
TOKEN = "your-token"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

def check_rate_limit():
    """Check GitHub API rate limits and handle resets if necessary"""
    url = "https://api.github.com/rate_limit"
    response = requests.get(url, headers=HEADERS)
    rate_limit = response.json()
    remaining = rate_limit['rate']['remaining']
    reset_time = rate_limit['rate']['reset']

    if remaining == 0:
        wait_time = reset_time - time.time()
        print(f"Rate limit exceeded. Waiting for {wait_time:.2f} seconds.")
        time.sleep(wait_time + 1)
    else:
        print(f"Requests remaining: {remaining}")

def fetch_all_pages(fetch_function, *args, **kwargs):
    """Fetch all paginated results for a given API function"""
    all_results = []
    page = 1
    while True:
        print(f"Fetching page {page}...")
        check_rate_limit()
        results = fetch_function(*args, **kwargs, page=page)
        if not results:
            print("No more results to fetch.")
            break
        all_results.extend(results)
        page += 1
        time.sleep(0.5)
    return all_results

def search_repositories(query, per_page=10, page=1):
    """Search GitHub repositories using the Search API"""
    url = "https://api.github.com/search/repositories"
    params = {"q": query, "per_page": per_page, "page": page}
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Error: {response.status_code}")
        pprint(response.json())
        return []

def get_commits(owner, repo, per_page=10, page=1):
    """Fetch commits for a given repository"""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"per_page": per_page, "page": page}
    response = requests.get(url, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        pprint(response.json())
        return []

def get_contents(owner, repo, path=""):
    """Fetch contents of a repository"""
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        pprint(response.json())
        return []

def save_to_json(data, filename):
    """Save data to a JSON file"""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

# Fetch all repositories
all_repositories = search_repositories(query="python", per_page=5)
print(f"Total repositories fetched: {len(all_repositories)}")
save_to_json(all_repositories, "repositories.json")

# Fetch all commits
all_commits = fetch_all_pages(get_commits, owner="octocat", repo="Hello-World", per_page=5)
print(f"Total commits fetched: {len(all_commits)}")
save_to_json(all_commits, "commits.json")

# Fetch all repository contents
all_contents = get_contents(owner="Timons172", repo="Library-Management-System")
print(f"Total contents fetched: {len(all_contents)}")
save_to_json(all_contents, "contents.json")