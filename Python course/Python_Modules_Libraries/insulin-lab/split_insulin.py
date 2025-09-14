# split_insulin.py

# Read the cleaned preproinsulin sequence
with open("preproinsulin-seq-clean.txt", "r") as f:
    seq = f.read().strip()

print("Total sequence length:", len(seq))  # Should be 110

# Extract parts of the sequence
lsinsulin = seq[0:24]     # 1–24
binsulin = seq[24:54]     # 25–54
cinsulin = seq[54:89]     # 55–89
ainsulin = seq[89:110]    # 90–110

# Save each part into its own file
with open("lsinsulin-seq-clean.txt", "w") as f: f.write(lsinsulin)
with open("binsulin-seq-clean.txt", "w") as f: f.write(binsulin)
with open("cinsulin-seq-clean.txt", "w") as f: f.write(cinsulin)
with open("ainsulin-seq-clean.txt", "w") as f: f.write(ainsulin)

# Print results for verification
print("LS (24):", lsinsulin, "Length:", len(lsinsulin))
print("B  (30):", binsulin,  "Length:", len(binsulin))
print("C  (35):", cinsulin,  "Length:", len(cinsulin))
print("A  (21):", ainsulin,  "Length:", len(ainsulin))
