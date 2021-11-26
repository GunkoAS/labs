def generate_alphabet(offset, keyword):
  offset = offset % 33
  
  l = len(alphabet)
  alphabet_new = alphabet[l-offset:] + alphabet[:l-offset]

  for char in keyword:
    alphabet_new  = alphabet_new.replace(char, "")

  alphabet_new = alphabet_new[:offset] + keyword + alphabet_new[offset:]
  return alphabet_new

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
offset = int(input()) % len(alphabet)
keyword = input()

alphabet_new = generate_alphabet(offset, keyword)

inp = input()
for line in inp:
    for character in line:
      if character.isalpha():
        if character.islower():
          ind = alphabet.find(character)
          character = alphabet_new[ind]
        else:
          ind = alphabet.find(character.lower())
          character = alphabet_new[ind].upper()
      print(character, end="")