def encrypt(text, key):
  return shift_text(text, key)

def decrypt(text, key):
  return shift_text(text, -key)

def shift_text(text, key):
  result = ""
  key = key % 26
  
  for char in text:
       if char.isalpha():
            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")
            new_char = chr((ord(char) - start + key) % 26 + start)
            result += new_char
        else:
            result += char
return result
