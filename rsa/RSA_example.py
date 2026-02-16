import math
import two_random_primes

# Get message to encrypt
M = input("Enter the message to encrypt: ")

# Convert message to ASCII values
M_ascii = [ord(letter) for letter in M]

# Get two random primes
p, q = two_random_primes.get_two_random_primes()

# Compute n, phi, e, and d
n = p * q
phi = (p - 1) * (q - 1)

# Common choice for e
e = 65537

# Ensure e and phi are coprime
if math.gcd(e, phi) != 1:
    # Find the next suitable e
    for candidate in range(3, phi, 2):
        if math.gcd(candidate, phi) == 1:
            e = candidate
            break
        
d = pow(e, -1, phi)

C = []
# Encrypt each letter's ASCII code and store in C
for i, letter in enumerate(M_ascii):
    encrypted = pow(letter, e, n)
    C.append(encrypted)

# Decrypt each letter and verify
M_decrypted = []
for i, encrypted in enumerate(C):
    decrypted = pow(encrypted, d, n)
    M_decrypted.append(decrypted)

# Convert M_decrypted back to characters
M_decrypted_string = ''.join(chr(num) for num in M_decrypted)

# Construct dict to print values nicely
result = {
    "Original Message": M,
    "ASCII Representation": M_ascii,
    "Chosen Primes": (p, q),
    "Modulus n (p * q)": n,
    "Public Exponent e": e,
    "Private Exponent d (mod φ(n))": d,
    "Ciphertext C": C,
    "Decrypted Message ASCII": M_decrypted,
    "Decrypted Message": M_decrypted_string
}

# Print results
for key, value in result.items():
    print(f"{key}: {value}")