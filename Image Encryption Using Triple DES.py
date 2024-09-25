from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from PIL import Image
import io

# Function to pad the data to be a multiple of the block size (8 bytes for DES)
def pad(data):
    while len(data) % 8 != 0:
        data += b' '
    return data

# Function to encrypt the image
def encrypt_image(, key):
    # Open the image and convert it to bytes
    with Image.open(image_path) as img:
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format=img.format)
        img_bytes = img_byte_array.getvalue()
    
    # Pad the image bytes
    padded_data = pad(img_bytes)
    
    # Create a Triple DES cipher object and encrypt the data
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypted_data = cipher.encrypt(padded_data)
    
    return encrypted_data

# Function to decrypt the image
def decrypt_image(encrypted_data, key, output_path, format):
    # Create a Triple DES cipher object and decrypt the data
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).rstrip(b' ')
    
    # Convert bytes back to an image and save it
    image = Image.open(io.BytesIO(decrypted_data))
    image.save(output_path, format=format)

# Example usage
key = get_random_bytes(24)  # 24 bytes for Triple DES (3 * 8 bytes)
encrypted_image = encrypt_image('input_image.jpg', key)
decrypt_image(encrypted_image, key, 'output_image.jpg', 'JPEG')
