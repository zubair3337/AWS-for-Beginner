#numbers=[10, 0, -1, 7]
#names=["tom", "jerry", "jhonney"]
#mix_lsit=[1, "jerry", True, 10.10]
#print(numbers)
#print(names)
#print(mix_lsit)
#print(numbers[1])


#list

# Create a list
favorite_fruits = ["apple", "banana", "mango"]
print("My favorite fruits:", favorite_fruits)

# Add a fruit
favorite_fruits.append("orange")
print("After adding a fruit:", favorite_fruits)

# Remove a fruit
favorite_fruits.remove("banana")
print("After removing a fruit:", favorite_fruits)

# Replace a fruit
favorite_fruits[1] = "grapes"
print("After replacing a fruit:", favorite_fruits)

# Check if a fruit is in the list
if "apple" in favorite_fruits:
    print("Yes, 'apple' is one of my favorite fruits!")

# Print all fruits
print("Here are all my favorite fruits:")
for fruit in favorite_fruits:
    print(fruit)

# Count the number of fruits
print("I have", len(favorite_fruits), "favorite fruits.")
