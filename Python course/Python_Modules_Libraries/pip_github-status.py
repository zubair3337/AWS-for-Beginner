import requests

url = "https://api.github.com"
response = requests.get(url)

print("GitHub API Status Code:", response.status_code)
