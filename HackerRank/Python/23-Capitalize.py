# Problem
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalized correctly as Alison Heck.

# alison heck  – Alison Heck

# Given a full name, your task is to capitalize the name appropriately.

# Input Format
# A single line of input containing the full name, S.

# Constraints
# 0 < len(S) < 1000
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

# Output Format
# Print the capitalized string, S.

#-----------------------------------------------------------

# Sorun
# Kişilerin pasaportlarında ad ve soyadlarının büyük harfle başlamasını sağlamanız istenmektedir. Örneğin, alison heck, Alison Heck olarak doğru bir şekilde büyük harfle yazılmalıdır.

# Alison Heck – Alison Heck

# Tam bir ad verildiğinde, göreviniz adı uygun şekilde büyük harfle yazmaktır.

# Giriş Formatı
# S tam adını içeren tek bir giriş satırı.

# Kısıtlamalar
# 0 < mercek(S) < 1000
# Dize alfasayısal karakterlerden ve boşluklardan oluşur.
# Not: Bir kelimede sadece ilk karakter büyük harfle yazılır. Örnek 12abc, büyük harfle yazıldığında 12abc olarak kalır.

# Çıkış formatı
# Büyük harfle yazılan S dizesini yazdırın.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()