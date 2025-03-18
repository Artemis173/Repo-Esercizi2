from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys
from PIL import Image
from io import BytesIO

def decrypt_aes(image_path, key):
    # Leggi il file cifrato
    with open(image_path, "rb") as f:
        encrypted_data = f.read()

    print(f"Length of encrypted data: {len(encrypted_data)} bytes")  # Lunghezza dei dati cifrati

    # Aggiungi padding manuale se la lunghezza non è un multiplo di 16
    if len(encrypted_data) % 16 != 0:
        print("Warning: Data length is not a multiple of 16 bytes, adding padding manually.")
        encrypted_data = encrypted_data + b'\x00' * (16 - len(encrypted_data) % 16)

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)

    # Rimuovi il padding
    padding_length = decrypted_data[-1]
    if padding_length > 0 and padding_length <= 16:
        decrypted_data = decrypted_data[:-padding_length]

    # Stampa i primi byte per vedere se sono corretti
    print(f"First 16 bytes of decrypted data: {decrypted_data[:16]}")

    # Tentativo di apertura dell'immagine
    try:
        image = Image.open(BytesIO(decrypted_data))  # Leggi i dati come immagine
        image.show()  # Mostra l'immagine
        output_path = "decrypted_image.png"
        image.save(output_path)  # Salva l'immagine decrittografata
        print(f"AES Decryption complete: {output_path}")
    except Exception as e:
        print(f"Error opening image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python decrypt_aes.py <encrypted_image.png>")
        sys.exit(1)

    image_path = sys.argv[1]
    aes_key = b"thisisatestkey12"  # 16-byte AES key (for AES-128)

    print("Attempting AES decryption...")
    try:
        decrypt_aes(image_path, aes_key)
    except Exception as e:
        print(f"AES decryption failed: {e}")
