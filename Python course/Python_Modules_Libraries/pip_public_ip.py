import requests

# API that returns only IPv4 address
url = "https://api.ipify.org?format=json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("🌍 Your Public IPv4 is:", data["ip"])
else:
    print("⚠️ Couldn't fetch IPv4. Status:", response.status_code)
