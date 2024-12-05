# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# Per iniziare generiamo una coppia di chiavi e le stampiamo
# enerating RSA Key Pair
# Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)
sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAwL+/Kd2tmiQFUq24JuWC/a2bzr7e5NQvTf+EldoNhlHqGqnq\n6HK7HkW2DlTxH21fE0UcZeBKcT9cxDwJYw9dN2s8tnvZjH7IeklngBx17KeuOlVN\nUvD7Z3HN+49wTG/M6mj8jPGZtcW0u1ODX593cwiToM1byhP2KmzCf8AUfBAKmbbn\nJUNEDw+3/mTRLftDB4ULGtlp/QVH7hxUrmOe5Ta1RJ5LVdCmHpIiklCoJRlLd2ed\nwAi5A/kRTZROMTKu5FCFXSe97P30uLB+c+jIQOMiN0E0Ywd4mpYEwdBNZKqwyqhj\n79ismxRJz4GAvxDNuR1WDx1aCnf6DCHMRbRffQIDAQABAoIBACDI7J/XIiZv/ozJ\n2iMZkj6KZ1BS9HA5LCOo9NkVSgwhBkALS1bG3w9+3YDSD2JgVNXfAT3N2POqyqFh\nMdqM3DbnMWA7sCz+yqRMNIPcs20xt0eaR0j2jtiRSa9CfmAt+w2bFmv100aRDpT3\nV0buRZ/GI3AsRfLZEtuz/KBEoGdaejgAN0tNPsarLTrCvAd7nGvTRUP27qw0ERqL\nWZtAZAemLRtCxZ+N3pqyHCk6Xm0KxAClGcDpSVhLgXz9GECfcf3dfUXPHC7QGYli\njCAJxGLp6xR0aGBX3GK8NkkSGSdFBO3Cykc5UE7/GSVpKwtlOFWzczGYxCU4gOlD\nhWFg2KECgYEAyU1CLCQCPEgeFld44+Ixmik1wm63dAy+irBRl/QT/qyWdhQuo6hp\nuk3RDMBkOYkS3hLMhr6U0HIpbdUoCMIYTRvZrohRwT+xcBXxqOoqfgZB0gf3cUJH\n7RSugM7v/7/DpmLgK3sZ07WVeLzviKMH9glYv7ZALePStvs38oJ9Ox0CgYEA9R+M\nf6Cwk6qg9OiQIMGdHuIAscviJgB5DJV95E/YDPAjEY2HYASiyzb2T4SwyCorkprF\n2oVBZuHzsvXrscYInxTx4lX9XfFJdKhwXIgqu95iC0BkTul3HOiRGizvZdjM1SpW\n0pw+Y9uvgud39M0RaLbdB9FP6b3IVSx/EfSKJ+ECgYEAt3fdzsNG8lA8c9pniTM4\nSCw1Hi+wrmmLJHZM93Ry4NPGEnqUg37UVgPke33CGxpOgu6ZUFnU4iKalcsHwOu+\nIFE41jTSZpI5k1G8vlomPlRPmzC9mpFxYqhN34I8BVlu5XAKpjZ9NJK0V6XDn0IP\n2HNuWtStq+WPwEw5EqNRphUCgYEA3vR1PNkSAx5eDKVEAydYHHEApLeH2XzwnYuT\n2IjvQMVjgGG00pck46X4X9eXXFlPDKgOcnZmSIgYu5yHZ0lzKg9I+8+vBzWi1KMo\noGGSTRM3JnjJRCWCnB7FbIOWtJJ/rRw3oJVRAk8d0vlq2JV10kMRxDyUbUyb3Sz9\n330H9MECgYBBN9TAGVtGMeW1Tg+NIUMX0xZ5QJAmn3tOZF9FejvMkdxkZIde+JAU\nU5mQZDnZ9vwR493RrNqSgPVv/AKkcuWtm/2vWK0D+Hyeflph8+psXJzO+Bkoytxa\nrYSzc40pE+mnT6/uf/DhkiIVx7Jeyk6t1VeQH2nIDnDhbeN9e/ptWQ==\n-----END RSA PRIVATE KEY-----"
sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwL+/Kd2tmiQFUq24JuWC\n/a2bzr7e5NQvTf+EldoNhlHqGqnq6HK7HkW2DlTxH21fE0UcZeBKcT9cxDwJYw9d\nN2s8tnvZjH7IeklngBx17KeuOlVNUvD7Z3HN+49wTG/M6mj8jPGZtcW0u1ODX593\ncwiToM1byhP2KmzCf8AUfBAKmbbnJUNEDw+3/mTRLftDB4ULGtlp/QVH7hxUrmOe\n5Ta1RJ5LVdCmHpIiklCoJRlLd2edwAi5A/kRTZROMTKu5FCFXSe97P30uLB+c+jI\nQOMiN0E0Ywd4mpYEwdBNZKqwyqhj79ismxRJz4GAvxDNuR1WDx1aCnf6DCHMRbRf\nfQIDAQAB\n-----END PUBLIC KEY-----"
sPubEmanuele = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuVul4pu+fJI1maIbkbz0\n7JKwwUqQHjS+I6YoqLRy68OJ3n+8R1HzvOFcqaZ0+Kbv0YxbALTurBXzpwXzOtuj\n42cY0Yc9Fb0VutZ7JJm0UEaTRgiZjBm05D6fXgl0RhT/lcmJZL8RJNWEPztnJXcn\nY76/1Ksrzk72ejjJwInxUWKt44/lKg1YbNDk+KwGotwr1Cw5BGHh92um1DSEqyko\ntUcEhT/CSf80VCzpZ056FTvms+7TOet4tMEEw5DRZpCzQQI1Fo2LuPPHi99s7Wtf\nvGCgXIYTJhdoAUHb3hgA968iecogntBEvn+tp8LLGVktDZF0LLAwCS5Fz80MfUj3\naQIDAQAB\n-----END PUBLIC KEY-----"

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
public_key_emanuele = RSA.import_key(sPubEmanuele)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# # Example usage
# message = "This is a secret message"
# encrypted_message = encrypt_message(message, public_key)
# decrypted_message = decrypt_message(encrypted_message, key_pair)

# print("Original Message:", message)
# print("Encrypted Message:", encrypted_message)
# print("Decrypted Message:", decrypted_message)

m = "Ciao"
c = encrypt_message(m, public_key_emanuele)
print(c)
em = " "
d = decrypt_message(em, key_pair)
print(d)