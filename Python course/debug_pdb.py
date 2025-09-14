

# ********* commands in pdb module debugging ********
# 1. n -> used to execute line and move in next line
# 2. l -> used to check in which line pdb is present
# 3. varibale_name -> used to check variable is exist and have info correctly
# 4. c -> used to continue run whole code normally
# 5. q -> used to quit from debugger


import pdb
pdb.set_trace()
a = 10
b = 50
d = (a + b) / c
print(d)


# actual code

# a = 10
# b = 50
# c = 0

# if c != 0:
#     d = (a + b) / c
#     print(d)
# else:
#     print("Error: Division by zero is not allowed.")
