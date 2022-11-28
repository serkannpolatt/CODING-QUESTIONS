# Task
# You are given a string S.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

# Input Format
# A single line containing the string S and integer value k separated by a space.

# Constraints
# 0 < k <= len(S)
# The string contains only UPPERCASE characters.
# Output Format
# Print the combinations with their replacements of string S on separate lines.


# Sample Input

# HACK 2
# Sample Output

# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

#-------------------------------------------------------------

# Görev
# Size bir S dizisi verilir.
# Göreviniz, dizgenin olası tüm k boyutu değiştirme kombinasyonlarını sözlükbilimsel olarak sıralanmış bir sırayla yazdırmaktır.

# Giriş Formatı
# Bir boşlukla ayrılmış S dizesini ve k tamsayı değerini içeren tek bir satır.

# Kısıtlamalar
# 0 < k <= len(S)
# Dize yalnızca BÜYÜK HARF karakterleri içerir.
# Çıkış formatı
# Kombinasyonları, S dizesinin yer değiştirmeleriyle ayrı satırlara yazdırın.


# Örnek Giriş

# HACK 2
# Örnek Çıktı

# AA
# AC
#AH
# AK
# Bilgi
# CH
# CK
# SS
# Türkiye
# KK

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S, k = map(str, input().split())

S = sorted(S)
k = int(k)

for e in list(combinations_with_replacement(S, k)):
    print(*e, sep='')