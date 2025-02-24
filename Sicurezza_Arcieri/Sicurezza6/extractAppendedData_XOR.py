import base64

def caesar_shift_binary(text, shift):
    result = bytearray()
    for c in text:
        result.append((c + shift) % 256)
    return result

def caesar_shift_text(text, shift):
    result = bytearray()
    for c in text:
        if 65 <= c <= 90:  # Uppercase letters
            result.append((c - 65 + shift) % 26 + 65)
        elif 97 <= c <= 122:  # Lowercase letters
            result.append((c - 97 + shift) % 26 + 97)
        else:
            result.append(c)  # Non-alphabetic characters remain unchanged
    return result


# with open("img1.png", "ab") as f:
#     # primo esempio
#     f.write(b"Hello, World!")

# with open("img2.png", "ab") as f:
#     #secondo esempio
#     encoded_string = base64.b64encode(b"Hello, World!")
#     f.write(encoded_string)

# with open("img3.png", "ab") as f:
#     #terzo esempio (cesare testo)
#     shifted_text = caesar_shift_text(b"Hello, World!", 3)
#     f.write(shifted_text)

# with open("img4.png", "ab") as f:
#     #quarto esempio (xor binario)
#     v=[]
#     for c in b"Hello, World!":
#         v.append(c ^ 0x55)
#     v = bytearray(v)
#     f.write(v)

# with open("img5.png", "ab") as f:
#     #quinto esempio (cesare binario)
#     shifted_binary = caesar_shift_binary(b"Hello, World!", 3)
#     f.write(shifted_binary)

# with open("img6.png", "ab") as f:
#     #sesto esempio, append di una seconda immagine
#     with open("addimg.png", "rb") as g:
#         f.write(g.read())
        


from PIL import Image
import numpy as np


# Convert a string to a stream of bits
def string_to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:].zfill(8)
        result.extend([int(b) for b in bits])
    return result

def ModifyBits1(image_path, output_path):
    # Load the image
    image = Image.open(image_path).convert("RGB")  # Convert to RGB mode

    # Convert image to NumPy array (matrix)
    image_matrix = np.array(image)

    # Example usage
    bit_stream = string_to_bits("Hello, World!")

    # qui modifico bit
    for i in range(len(bit_stream)):
        # Set the least significant bit to the corresponding bit in the bit stream
        image_matrix[i] &= 0xFE
        image_matrix[i] |= bit_stream[i]

    # Convert back to image
    modified_image = Image.fromarray(image_matrix)

    # Save the modified image
    modified_image.save(output_path)

ModifyBits1("img7.png", "img7dat.png")

def ModifyImage(image_path, output_path):
    # Load the image
    image = Image.open(image_path).convert("RGB")  # Convert to RGB mode

    # Convert image to NumPy array (matrix)
    image_matrix = np.array(image)

    # XOR the image matrix with numbers from 0 to 0xFF
    for i in range(image_matrix.shape[0]):
        for j in range(image_matrix.shape[1]):
            for k in range(image_matrix.shape[2]):
                image_matrix[i, j, k] ^= (i + j + k) % 256

    modified_image = Image.fromarray(image_matrix)
    modified_image.save(output_path)



ModifyImage("img7.png", "img7new.png")
