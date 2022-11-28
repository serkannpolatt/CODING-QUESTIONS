# Task
# You are given three integers: a, b, and m. Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

# Input Format
# The first line contains a, the second line contains b, and the third line contains m.

# Constraints
# 1 <= a <= 10
# 1 <= b <= 10
# 2 <= m <= 1000
# Sample Input


# 3
# 4
# 5
# Sample output

# 81
# 1

#-------------------------------------------------------------

# Görev
# Size üç tam sayı verilir: a, b ve m. İki satır yazdırın.
# İlk satıra pow(a,b) sonucunu yazdırın. İkinci satırda, pow(a,b,m) sonucunu yazdırın.

# Giriş Formatı
# İlk satırda a, ikinci satırda b ve üçüncü satırda m bulunur.

# Kısıtlamalar
# 1 <= bir <= 10
# 1 <= b <= 10
# 2 <= m <= 1000
# Örnek Giriş


# 3
# 4
# 5
# Örnek çıktı

# 81
# 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

a = int(input())
b = int(input())
m = int(input())

c = math.pow(a, b)
d = c%m

print(int(c))
print(int(d))