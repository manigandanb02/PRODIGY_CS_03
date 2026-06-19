# 🔐 PixelCrypt – Image Encryption Tool

## 📖 Overview

PixelCrypt is a Python-based Image Encryption Tool featuring image encryption and decryption, pixel manipulation, key-based pixel shuffling, mathematical pixel transformations, secret key processing, and reversible image recovery.

This project was developed as part of the Prodigy InfoTech Cyber Security Internship Program.

---

# Image Encryption Concept

Image encryption is the process of transforming an image into a modified format so that its visual content becomes unreadable without applying the correct decryption process.

This can be achieved by altering pixel values, rearranging pixel positions, or combining multiple transformation techniques. The original image can then be recovered by reversing the same operations.

PixelCrypt demonstrates image encryption by:

* Reading image data and extracting pixel values
* Applying secret key-based transformations to image pixels
* Rearranging pixel positions to generate an encrypted image
* Reversing the transformations to recover the original image

---

# ✨ Features

## Image Encryption

* Encrypts images using a secret key
* Modifies RGB pixel values
* Rearranges pixel positions

## Image Decryption

* Restores encrypted images
* Reverses pixel shuffling
* Recovers original RGB values

## Pixel Manipulation

* Processes RGB channels individually
* Applies transformations to pixel values

## Key-Based Pixel Shuffling

* Randomizes pixel positions using a user-defined key
* Uses deterministic shuffling for accurate recovery

## Reversible Encryption Process

* Allows encrypted images to be restored using the same key
* Maintains image dimensions and structure

---

# 🛠️ Technologies Used

* Python
* Pillow (PIL)
* Python Random Module
* File Handling

---

# 📂 Project Structure

```text
PixelCrypt/
│
├── image_encrypt.py
│
└── images/
    ├── original/
    ├── encrypted/
    └── decrypted/
```

---

# ⚙️ Installation

Install the required dependency:

### Windows

```bash
py -m pip install Pillow
```

### Linux (Ubuntu)

```bash
python3 -m pip install Pillow
```

---

# 🚀 How to Run

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/manigandanb02/PRODIGY_CS_03.git PixelCrypt
```

## 2️⃣ Navigate to the Project Folder

```bash
cd PixelCrypt
```

## 3️⃣ Run the Program

### Windows

```bash
python image_encrypt.py
```

### Linux (Ubuntu)

```bash
python3 image_encrypt.py
```

---

# 🔐 Encryption Process

During encryption:

1. Read the input image
2. Extract RGB pixel values
3. Apply secret key-based pixel transformation
4. Shuffle pixel positions
5. Generate encrypted image

```text
Original Image
      ↓
Read RGB Pixels
      ↓
Apply Pixel Transformation
      ↓
Shuffle Pixels
      ↓
Encrypted Image
```

---

# 🔓 Decryption Process

During decryption:

1. Read the encrypted image
2. Restore shuffled pixel positions
3. Reverse pixel transformations
4. Recover original image

```text
Encrypted Image
       ↓
Restore Pixel Order
       ↓
Reverse Pixel Transformation
       ↓
Decrypted Image
```

> ⚠️ The same secret key used during encryption must be provided during decryption. Otherwise, the original image cannot be recovered correctly.

---

# 📚 Learning Outcomes

Through this project, I learned:

* Fundamentals of image encryption
* RGB pixel representation
* Pixel manipulation techniques
* Image processing using Pillow
* Key-based pixel shuffling
* Reversible encryption and decryption
* File handling in Python
* Command-line application development
* Secure data transformation concepts

---

# ⚠️ Disclaimer

This project is developed for educational purposes and cybersecurity learning.

The encryption technique implemented in this project demonstrates basic image encryption concepts using pixel-level transformations and key-based pixel shuffling. It is intended to showcase image processing and reversible encryption techniques rather than provide modern cryptographic image security.
