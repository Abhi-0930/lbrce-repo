def count_words(word):
  count = 0
  a = word.split()
  for i in a:
    count += 1
  return count

word = str(input())
count_words(word)