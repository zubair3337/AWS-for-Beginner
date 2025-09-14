# Using pip to install and use third-party modules
# Run this command in terminal (like downloading from Play Store):
# pip install requests

import requests  # extra tool downloaded from "Python Play Store"

# Example: checking if GitHub website is alive (like pinging a friend)
response = requests.get("https://api.github.com")
print("GitHub API Status Code:", response.status_code)
