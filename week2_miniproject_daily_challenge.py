# -*- coding: utf-8 -*-
"""week2/miniproject/daily_challenge.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11dZTOLCISBtwKzzMiqS5XvsovS20I5o9
"""

my_string= 'without,hello,bag,world'
sorted_string = ','.join(sorted([word for word in my_string.split(',')]))

print(sorted_string)

my_string = "Margaret's toy is a pretty doll."
def longest_word(sentence):
    words = sentence.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word(my_string))