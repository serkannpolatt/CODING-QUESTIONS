# Task
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

# Input Format
# A single line containing the string S and integer value k separated by a space.

# Constraints
# 0 < k < len(S)
# The string contains only UPPERCASE characters.
# Output Format
# Print the different combinations of string S on separate lines.


# Sample Input

# HACK 2
# Sample Output

# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

#-------------------------------------------------------------

# Görev
# Size bir S dizisi verilir.
# Göreviniz, dizgenin k boyutuna kadar tüm olası kombinasyonlarını sözlükbilimsel olarak sıralanmış sırada yazdırmaktır.

# Giriş Formatı
# Bir boşlukla ayrılmış S dizesini ve k tamsayı değerini içeren tek bir satır.

# Kısıtlamalar
# 0 < k < len(ler)
# Dize yalnızca BÜYÜK HARF karakterleri içerir.
# Çıkış formatı
# S dizisinin farklı kombinasyonlarını ayrı satırlara yazdırın.


# Örnek Giriş

# HACK 2
# Örnek Çıktı

# A
# C
# H
# K
# AC
#AH
# AK
# CH
# CK
# Türkiye

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s , n  = input().split()
for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))