import sys
import base64
import jwt

# Get location of key
if len(sys.argv) < 3:
    print("Usage: python jwt.py <path to private key> <path to public key")
    sys.exit(1)

private_key_loc = sys.argv[1]
public_key_loc = sys.argv[2]

# Read key into memory
with open(private_key_loc, "rb") as f:
    private_key = f.read()

# Encode a JWT
example_payload = {"my": "data"}
encoded = jwt.encode(example_payload, private_key, algorithm="RS512")

print(encoded.decode("utf-8"))

# Get public key
with open(public_key_loc, "rb") as f:
    public_key = f.read()

# Decode the JWT
decoded = jwt.decode(encoded, public_key, algorithms="RS512")

print(f"Original payload:\n{example_payload}")
print(f"Decoded payload:\n{decoded}")
