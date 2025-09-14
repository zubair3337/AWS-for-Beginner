import re

# Open the file
with open("preproinsulin-seq.txt", "r") as f:
    raw_seq = f.read()

# Remove unwanted parts
clean_seq = re.sub(r"[^a-zA-Z]", "", raw_seq)  # keep only letters

print("Cleaned sequence:", clean_seq)
print("Length of sequence:", len(clean_seq))
