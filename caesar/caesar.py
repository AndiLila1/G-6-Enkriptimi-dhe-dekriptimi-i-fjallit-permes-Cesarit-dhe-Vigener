def shift_text(text, key):
  result = ""
  key = key % 26
  
  for char in text:
       if char.isalpha():
            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")
        else:
            result += char
