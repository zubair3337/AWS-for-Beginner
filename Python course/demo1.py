# test_requests.py
# Practice script to check if the "requests" module is installed and working

try:
    import requests
    print("✅ The 'requests' module is installed.")

    # Make a simple request to GitHub API
    response = requests.get("https://api.github.com")

    # Check status
    if response.status_code == 200:
        print("🌍 Successfully fetched data from the internet using requests!")
        print("GitHub API message:", response.json()["current_user_url"])
    else:
        print("⚠️ Something went wrong. Status code:", response.status_code)

except ImportError:
    print("❌ The 'requests' module is NOT installed. Run:")
    print("   pip install requests")
except Exception as e:
    print("⚠️ An error occurred while testing requests:", e)
