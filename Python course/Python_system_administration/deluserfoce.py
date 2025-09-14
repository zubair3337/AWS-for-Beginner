import os
import pwd

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ").strip()
        print(f"Remove the user '{username}' and delete their home directory + group? (Y/N)")
        confirm = input().strip().upper()

    try:
        # First remove the user and home directory
        os.system(f"sudo deluser --remove-home {username}")

        # Try to get the user's primary group before it's removed
        try:
            user_info = pwd.getpwnam(username)
            groupname = user_info.pw_name  # usually same as username
        except KeyError:
            groupname = None

        # Remove the user's group (if it exists)
        if groupname:
            os.system(f"sudo delgroup {groupname}")

        # Extra cleanup: find any leftover files owned by the user
        print("Searching for leftover files...")
        os.system(f"sudo find / -user {username} -exec ls -ld {{}} \\; 2>/dev/null")

        print(f"✅ User '{username}' and related data removed successfully.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    remove_user()
