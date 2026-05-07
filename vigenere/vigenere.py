def encrypt(text, key):
    return vigenere_cipher(text, key, "encrypt")


def decrypt(text, key):
    return vigenere_cipher(text, key, "decrypt")

def vigenere_cipher(text, key, operation):
    result = ""
    key = "".join(char.lower() for char in key if char.isalpha())
    if not key:
        raise ValueError("Key must contain at least one letter.")

    key_index = 0

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")

            shift = ord(key[key_index % len(key)]) - ord("a")
            if operation == "decrypt":
                shift = -shift

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
            key_index += 1
        else:
            result += char

    return result
