# -*- coding: utf-8 -*-
"""question.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFC87gMrg7ivxsi55tjpanG1qUb-kMRt
"""

word = input('Enter the word:')
#You should write the code below to don't confuse about small and big characters!
word = word.upper()

word_box = []
listt = []

#We have seperated word from duplicated duplicated characters
for i in range(len(word)-1):
  if i==0 and word[i+1] != word[i]:
    listt.append(word[i])
    listt.append(word[i+1])
  elif i!=0 and word[i+1] != word[i]:
    listt.append(word[i+1])
  else:
    word_box.append(listt)
    listt=[word[i+1]]
word_box.append(listt)

#Defining the longest word and it's length
def chooseMaxLengthWord():
  longest_word_list = []
  for i in word_box:
    if len(i) >= len(longest_word_list):
      longest_word_list = i
  longest_word = "".join(longest_word_list)
  print(f"Output: {longest_word} Length:{len(longest_word)}")


chooseMaxLengthWord()