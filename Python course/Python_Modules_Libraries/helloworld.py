# helloworld.py
# Demonstrates using JSON, if statements, and try/except for flow control

import json

filename = "userName.json"
name = ""

# 1. Check for a history file
try:
    with open(filename, "r") as r:
        # Load the user's name from the history file
        name = json.load(r)
except IOError:
    print("First-time login")

# 2. If the user was found in the history file, welcome them back
if name != "":
    print("Welcome back, " + name + "!")
else:
    # If the history file doesn't exist, ask the user for their name
    name = input("Hello! What's your name? ")
    print("Welcome, " + name + "!")

    # 3. Save the user's name to the history file
    try:
        with open(filename, "w") as f:
            json.dump(name, f)
    except IOError:
        print("There was a problem writing to the history file.")
