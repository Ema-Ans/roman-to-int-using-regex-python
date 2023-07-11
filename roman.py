# First make a dictionary that will store these values:
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# IX - 9
# IV - 4
# XL - 40
# XC - 90
# CD - 400
# CM - 900

import re

def split(s):
    pattern = r'(CM|CD|XC|XL|IV|IX|M|D|C|L|X|V|I)'
    result = re.findall(pattern, s)
    return result
    

def romanToInt(s):
    
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M' : 1000, 
               'IX': 9, 'IV': 4, 'XL': 40 , 'XC': 90, 'CD': 400, 'CM': 900}
    my_list = split(s)
    my_int = 0
    for elem in my_list:
        my_int += my_dict[elem]
    return my_int


