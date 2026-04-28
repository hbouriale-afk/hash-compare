import hashlib

def sha256_file(filename):
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).digest()

def count_identical_bits(h1, h2):
    identical = 0
    for b1, b2 in zip(h1, h2):
        diff = b1 ^ b2
        identical += 8 - bin(diff).count("1")
    return identical

file1 = "F1.txt"
file2 = "F2.txt"

h1 = sha256_file(file1)
h2 = sha256_file(file2)

identical_bits = count_identical_bits(h1, h2)

print("Hash 1:", h1.hex())
print("Hash 2:", h2.hex())
print("Identical bits:", identical_bits)
print("Different bits:", 256 - identical_bits)