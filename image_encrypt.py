from PIL import Image
import os
import random


def generate_shuffle_indices(length, key):
    random.seed(key)
    indices = list(range(length))
    random.shuffle(indices)
    return indices


def encrypt_image():
    image_path = input("Enter image path: ").strip()

    if not os.path.exists(image_path):
        print("Image not found!")
        return

    try:
        key = int(input("Enter encryption key (0-255): "))
    except ValueError:
        print("Invalid key!")
        return

    if key < 0 or key > 255:
        print("Key must be between 0 and 255!")
        return

    image = Image.open(image_path).convert("RGB")
    try:
        pixels = list(image.get_flattened_data())
    except AttributeError:
        pixels = list(image.getdata())

    encrypted_pixels = []

    for r, g, b in pixels:
        encrypted_pixels.append((
            (r + key) % 256,
            (g + key) % 256,
            (b + key) % 256
        ))

    indices = generate_shuffle_indices(len(encrypted_pixels), key)

    shuffled_pixels = [None] * len(encrypted_pixels)

    for i, shuffled_index in enumerate(indices):
        shuffled_pixels[shuffled_index] = encrypted_pixels[i]

    encrypted_image = Image.new("RGB", image.size)
    encrypted_image.putdata(shuffled_pixels)

    os.makedirs("images/encrypted", exist_ok=True)

    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)

    output_path = f"images/encrypted/{name}_encrypted{ext}"

    encrypted_image.save(output_path)

    print("\nImage encrypted successfully!")
    print(f"Saved to: {output_path}")


def decrypt_image():
    image_path = input("Enter encrypted image path: ").strip()

    if not os.path.exists(image_path):
        print("Image not found!")
        return

    try:
        key = int(input("Enter decryption key (0-255): "))
    except ValueError:
        print("Invalid key!")
        return

    if key < 0 or key > 255:
        print("Key must be between 0 and 255!")
        return

    image = Image.open(image_path).convert("RGB")
    try:
        pixels = list(image.get_flattened_data())
    except AttributeError:
        pixels = list(image.getdata())

    indices = generate_shuffle_indices(len(pixels), key)

    unshuffled_pixels = [None] * len(pixels)

    for i, shuffled_index in enumerate(indices):
        unshuffled_pixels[i] = pixels[shuffled_index]

    decrypted_pixels = []

    for r, g, b in unshuffled_pixels:
        decrypted_pixels.append((
            (r - key) % 256,
            (g - key) % 256,
            (b - key) % 256
        ))

    decrypted_image = Image.new("RGB", image.size)
    decrypted_image.putdata(decrypted_pixels)

    os.makedirs("images/decrypted", exist_ok=True)

    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)

    output_path = f"images/decrypted/{name}_decrypted{ext}"

    decrypted_image.save(output_path)

    print("\nImage decrypted successfully!")
    print(f"Saved to: {output_path}")


def main():
    while True:
        print("\n" + "=" * 45)
        print("      PIXELCRYPT - IMAGE ENCRYPTION TOOL")
        print("=" * 45)
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            encrypt_image()

        elif choice == "2":
            decrypt_image()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
