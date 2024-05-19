# -*- coding: utf-8 -*-
"""2week/day2/challenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17HH3aa1F2JYnbZDztAaKJauPgz_nsHw_
"""

def convert_to_list_of_char_lists_ignore_newlines(s):
    result = []
    i = 0
    while i < len(s):
        while i < len(s) and (s[i] == ' ' or s[i] == '\n'):
            i += 1
            continue
        if i >= len(s):
            break

        group = s[i:i+3]

        group = group.replace('\n', ' ')
        if len(group) < 3:
            group = group.ljust(3)
        char_list = list(group)
        result.append(char_list)
        i += 3
    return result

input_string = '''7ii
    Tsx
    h%?
    i #
    sM
    $a
    #t%
    ^r!'''
list_of_char_lists = convert_to_list_of_char_lists_ignore_newlines(input_string)
print(list_of_char_lists)

def convert_to_alpha_string_with_spaces(list_of_char_lists):
    result_string = ""

    for position in range(3):

        for char_list in list_of_char_lists:

            if len(char_list) > position:

                if char_list[position].isalpha():

                    result_string += char_list[position]
                else:

                    result_string += ' '
            else:

                result_string += ' '

    return result_string

alpha_string_with_spaces = convert_to_alpha_string_with_spaces(list_of_char_lists)
print(alpha_string_with_spaces)