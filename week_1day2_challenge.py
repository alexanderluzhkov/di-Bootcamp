# -*- coding: utf-8 -*-
"""week/1day2/challenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tFCMQMTV9Se69nrh6v_mrMVbX359GvWj
"""

while True:
  str_given = input('Tipe a string, pls. It has to consist of 10 characters. ')
  if len(str_given) ==10:
    print('perfect string')
    break
  elif len(str_given)< 10:
    print('Lengh is not enough')

  elif len(str_given)> 10:
    print('streeng is to long')
print(str_given[0],str_given[-1])
new_string=[]
for char in str_given:
  new_string.append(char)
  print(new_string)