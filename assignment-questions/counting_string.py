def count_string(string):
    vowel_count = 0
    consonant_count = 0
    digits_count = 0
    space_count = 0
    for char in string.lower():
        if char in "aeiou":
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char.isspace():
            space_count += 1
    return vowel_count, consonant_count, digits_count, space_count

string = str(input())
print(*count_string(string))