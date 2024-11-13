from Crypto.Cipher import AES
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
        return text

def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

key = "ThisIsASecretKey"
plain_text = "Hello, World!"
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)
print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

key2 = "IsASecretKey"
alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
texts: list = []
i : int = 0
while True:
    try:
        for i1 in range(26*2):
            for i2 in range(26*2):
                for i3 in range(26*2):
                    for i4 in range(26*2):
                        print(decrypt("OgJuOYJZT0FDb47DBOkNgA==", alphabet[i1]+alphabet[i2]+alphabet[i3]+alphabet[i4],key2))
    except:
        print(i)
        i += 1                    