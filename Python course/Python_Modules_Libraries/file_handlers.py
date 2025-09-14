# File Handling Example

# Writing to a file (like writing homework in a notebook)
file = open("example.txt", "w")
file.write("Hello, this is like writing notes in your notebook.\n")
file.write("Tomorrow you can read it back!")
file.close()

# Reading from the file (like reading your notes later)
file = open("example.txt", "r")
content = file.read()
print("Notebook content:")
print(content)
file.close()
