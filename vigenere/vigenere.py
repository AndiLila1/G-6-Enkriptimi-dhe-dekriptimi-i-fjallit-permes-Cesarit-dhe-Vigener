
def vigenere_cipher(text, key, operation):
    result = ""
    key = "".join(char.lower() for char in key if char.isalpha())
    if not key:
        raise ValueError("Key must contain at least one letter.")

    key_index = 0

    