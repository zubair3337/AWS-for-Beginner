import json
import os

filename = "savings.json"

# Load saved balance
if os.path.exists(filename):
    with open(filename, "r") as f:
        balance = json.load(f)
else:
    balance = 0  # start with empty piggy bank

print(f"🐷 Current Piggy Bank Balance: ₹{balance}")

# Add savings
amount = int(input("How much money do you want to add? ₹"))
balance += amount

# Save new balance
with open(filename, "w") as f:
    json.dump(balance, f)

print(f"✅ Saved! New Balance: ₹{balance}")
