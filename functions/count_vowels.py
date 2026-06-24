def count_vowels(word):
  count = 0
  for i in word.lower():
    if i in "aeiou":
      count += 1
  print(count)
word = str(input())
count_vowels(word)