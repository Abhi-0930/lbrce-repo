def first_non_repeating(string):
    lower_string = string.lower()
    for char in lower_string:
        if lower_string.count(char) == 1:
            return char
    return None

string = str(input())
print(first_non_repeating(string))