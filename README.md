🔐 Simple Encryption & Decryption
📌 Overview

This is a simple Python project that demonstrates message encryption and decryption using a random key-based Caesar cipher.
The program replaces each character in the input with another character based on a random shift value, and stores those shift values in a key.

⚙️ Features

Encrypt any text message (letters, numbers, symbols, punctuation).

Generate a random key for every encryption.

Decrypt the message back to its original form using the same key.

Preserves spaces between words.

🚀 How to Use

Run the script:

python Encryption.py


Enter the message you want to encrypt.

The program will output:

The encrypted message

The encryption key (list of random numbers)

To decrypt:

Paste the encrypted message when asked.

The program will use the stored key to recover the original message.

📝 Example
Enter the message for Encryption: Hello!
Encrypted message: Qb;?bV
Encryption key: [9, 14, 7, 10, 2, 19]

Enter the message to decrypt: Qb;?bV
Here is the message: Hello!

🔑 Important Notes

You must save the key that is generated during encryption. Without it, you cannot decrypt the message.

The encryption method is for learning purposes only and should not be used for securing sensitive data.
