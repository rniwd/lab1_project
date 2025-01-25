shift = int(input("Vvedite sdvig: "))
text = input("Vvedite tekst: ").split()
s = ''

for word in text:
    for char in word:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            elif char.islower():
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            s += new_char
        else:
            s += char
    s += ' '

print(s.strip())