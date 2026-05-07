def shift_text(text, key):
  result = ""
  key = key % 26
  
  for char in text:
       if char.isalpha():
            pass
        else:
            result += char
