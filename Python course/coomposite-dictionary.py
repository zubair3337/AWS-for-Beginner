#Composite Data Types: Useful for organizing and grouping complex, structured data (e.g., managing a system, collection, or entity relationships).

from datetime import datetime

# Composite data type: Dictionary
element_info = {
    "Top": 10,
    "Height": 200,
    "IsEmpty": False,
    "Left": 15,
    "Location": (15, 10),  # (Left, Top)
    "Right": 215,
    "Bottom": 210,
    "Size": (200, 200),    # (Width, Height)
    "Width": 200
}

# Access and display attributes
print(f"Top: {element_info['Top']}")
print(f"Height: {element_info['Height']}")
print(f"Is Empty: {element_info['IsEmpty']}")
print(f"Left: {element_info['Left']}")
print(f"Location: {element_info['Location']}")
print(f"Right: {element_info['Right']}")
print(f"Bottom: {element_info['Bottom']}")
print(f"Size: {element_info['Size']}")
print(f"Width: {element_info['Width']}")
