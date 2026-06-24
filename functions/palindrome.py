def palindrome(word):
  if word == word[::-1]:
    print("palindrome")
  else:
    print("not palindrome")

word = str(input())
palindrome(word)