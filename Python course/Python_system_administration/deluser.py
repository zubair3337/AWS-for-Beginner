import os

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ").strip()
        print(f"Remove the user '{username}'? (Y/N)")
        confirm = input().strip().upper()
    try:
        os.system(f"sudo deluser {username}")
        print(f"User '{username}' removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remove_user()
