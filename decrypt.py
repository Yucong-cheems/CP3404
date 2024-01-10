with open('ciphertext.txt', 'r') as file:
    ciphertext = file.read()


def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    key_length = len(key)

    for i, letter in enumerate(ciphertext):
        if letter.isalpha():
            # Convert letters to numbers from 0-25 and perform the decryption
            letter_num = ord(letter.upper()) - ord('A')
            key_num = ord(key[i % key_length].upper()) - ord('A')
            decrypted_num = (letter_num - key_num) % 26
            # Convert numbers back to letters and build the plaintext
            plaintext += chr(decrypted_num + ord('A'))
        else:
            plaintext += letter

    return plaintext

key = "problem"

plaintext = decrypt_vigenere(ciphertext, key)
print(f"Decrypted plaintext is:\n{plaintext}")
