import hashlib

data="ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"

for c in range(0x21, 0x7E):
    toCheck = chr(c).encode()
    hashed_password = hashlib.sha256(toCheck).hexdigest()
    if hashed_password == data:
        print(f"Password found: {chr(c)}")
        break