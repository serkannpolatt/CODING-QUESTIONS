# Task
# Read four numbers, a, b, c, and d, and print the result of ab + cd.

# Input Format
# Integers a, b, c, and d are given on four separate lines, respectively.

# Constraints
# 1 <= a <= 1000
# 1 <= b <= 1000
# 1 <= c <= 1000
# 1 <= d <= 1000
# Output Format
# Print the result of ab + cd on one line.

# Sample Input


# 9
# 29
# 7
# 27
# Sample Output

# 4710194409608608369201743232  
# Note: This result is bigger than 263 – 1. Hence, it won’t fit in the long long int of C++ or a 64-bit integer.

#-------------------------------------------------------------

# Görev
# Dört sayı, a, b, c ve d'yi okuyun ve ab + cd sonucunu yazdırın.

# Giriş Formatı
# a, b, c ve d tam sayıları sırasıyla dört ayrı satırda verilmiştir.

# Kısıtlamalar
# 1 <= bir <= 1000
# 1 <= b <= 1000
# 1 <= c <= 1000
# 1 <= d <= 1000
# Çıkış formatı
# ab + cd sonucunu bir satıra yazdırın.

# Örnek Giriş


# 9
# 29
# 7
# 27
# Örnek Çıktı

# 4710194409608608369201743232
# Not: Bu sonuç 263 – 1'den büyüktür. Bu nedenle, C++'ın uzun uzun int'sine veya 64 bit tam sayıya sığmaz.


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print((a**b)+(c**d))