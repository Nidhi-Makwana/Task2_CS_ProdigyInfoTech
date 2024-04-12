from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    try:
        # Open the image
        img = Image.open(image_path)

        # Convert the image to a NumPy array
        img_array = np.array(img)

        # Ensure key has the same shape as img_array
        key = np.resize(key, img_array.shape)

        # Encrypt each pixel using XOR with the key
        encrypted_array = np.bitwise_xor(img_array, key)

        # Convert the encrypted array back to an image
        encrypted_img = Image.fromarray(encrypted_array)

        # Save the encrypted image
        encrypted_img_path = os.path.splitext(image_path)[0] + "_encrypted.png"
        encrypted_img.save(encrypted_img_path)
        print("Image encrypted successfully.")
        return encrypted_img_path
    except Exception as e:
        print(f"Error encrypting image: {e}")
        return None


def decrypt_image(encrypted_image_path, key):
    try:
        # Open the encrypted image
        encrypted_img = Image.open(encrypted_image_path)

        # Convert the encrypted image to a NumPy array
        encrypted_array = np.array(encrypted_img)

        # Ensure key has the same shape as encrypted_array
        key = np.resize(key, encrypted_array.shape)

        # Decrypt each pixel using XOR with the key
        decrypted_array = np.bitwise_xor(encrypted_array, key)

        # Convert the decrypted array back to an image
        decrypted_img = Image.fromarray(decrypted_array)

        # Save the decrypted image
        decrypted_img_path = os.path.splitext(encrypted_image_path)[0] + "_decrypted.png"
        decrypted_img.save(decrypted_img_path)
        print("Image decrypted successfully.")
        return decrypted_img_path
    except Exception as e:
        print(f"Error decrypting image: {e}")
        return None


def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    # Input image path
    image_path = input("Enter the path to the image file: ")
    if not os.path.isfile(image_path):
        print("Invalid image path.")
        return

    # Generate a random key (you can use any integer as the key)
    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)

    # Encrypt the image
    encrypted_img_path = encrypt_image(image_path, key)

    if encrypted_img_path:
        # Decrypt the image
        decrypt_image(encrypted_img_path, key)


if __name__ == "__main__":
    main()
