import struct
import os
import argparse

def calculate_png_length(filepath):
    """Calculate the length of a PNG file based on its chunk structure."""
    PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
    
    with open(filepath, "rb") as f:
        # 1. Read and verify the PNG signature (8 bytes).
        signature = f.read(8)
        if signature != PNG_SIGNATURE:
            raise ValueError("Not a valid PNG file (wrong signature).")
        
        # We'll accumulate how many bytes we expect based on chunk data.
        # Start with 8 for the signature.
        total_length = 8
        
        while True:
            # 2. Read the next chunk length (4 bytes, big-endian).
            length_data = f.read(4)
            if len(length_data) < 4:
                # If we can't even read 4 bytes, the file is truncated.
                raise ValueError("Unexpected end of file (truncated chunk length).")
            
            chunk_length = struct.unpack(">I", length_data)[0]
            
            # 3. Read the chunk type (4 bytes ASCII).
            chunk_type = f.read(4)
            if len(chunk_type) < 4:
                raise ValueError("Unexpected end of file (truncated chunk type).")
            
            # 4. Skip the chunk data (chunk_length bytes).
            #    We don't need to process the data to count the length.
            f.seek(chunk_length, 1)  # move forward chunk_length bytes
            
            # 5. Skip the CRC (4 bytes).
            crc_data = f.read(4)
            if len(crc_data) < 4:
                raise ValueError("Unexpected end of file (truncated CRC).")
            
            # Update our total by:
            #   4 bytes (chunk length field)
            # + 4 bytes (chunk type)
            # + chunk_length bytes (the data)
            # + 4 bytes (CRC)
            total_length += (4 + 4 + chunk_length + 4)
            
            # 6. Check if we've just read the IEND chunk (end of PNG).
            if chunk_type == b"IEND":
                break
        
        return total_length

def shift_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep spaces, numbers, and symbols unchanged
    return result

# Implementazione compatta
s=lambda t,s:''.join([chr((ord(c)-(o:=(ord('A') if c.isupper() else ord('a')))+s)%26+o)if c.isalpha()else c for c in t])

if __name__ == "__main__":
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Calculate the length of a PNG file based on its chunk structure.")
        parser.add_argument("-i", "--infile", type=str, help="Path to the PNG file", required=True)
        parser.add_argument("-o", "--outfile", type=str, help="Name of the output file", required=True)
        return parser.parse_args()

    args = parse_arguments()
    path = args.infile
    out = args.outfile
    # Example usage:
    calculated_len = calculate_png_length(path)
    actual_len = os.path.getsize(path)

    print(f"Calculated PNG length: {calculated_len} bytes")
    print(f"Actual file size:       {actual_len} bytes")

    if calculated_len == actual_len:
        print("File size matches the PNG chunk structure.")
    else:
        print("Mismatch: the file may be corrupted or have extra data.")
        print("Extracting appended data...")
        with open(path, "rb") as f:
            # Skip the png data
            f.seek(calculated_len)
            appended_data = f.read(actual_len - calculated_len)
            with open(out, "wb") as f:
                f.write(appended_data)
    
    input_text = "Khoor, Zruog! "
    shift_value = 23
    encrypted_text = shift_cipher(input_text, shift_value)
    print(f"Encrypted text: {encrypted_text}")