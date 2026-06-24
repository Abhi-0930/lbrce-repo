# Determining whether a character is an alphabet, number, or special character.

ch = input()

if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
    print("Alphabet")
elif '0' <= ch <= '9':
    print("Number")
else:
    print("Special Character")