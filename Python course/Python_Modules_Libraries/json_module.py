# JSON Module Example

import json

# Example: packing student info into a JSON "lunchbox"
student = {
    "name": "Alice",
    "age": 20,
    "skills": ["Python", "AWS", "Drawing"]
}

# Convert to JSON (pack the lunchbox neatly)
json_string = json.dumps(student, indent=4)
print("Packed JSON lunchbox:")
print(json_string)

# Convert back to dictionary (unpack lunchbox to see items)
python_dict = json.loads(json_string)
print("\nUnpacked items from lunchbox:")
print(python_dict)
