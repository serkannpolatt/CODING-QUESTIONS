# Task
# Read in two integers, a and b, and print three lines.
# The first line is the integer division a//b (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: a%b.
# The third line prints the divmod of a and b.

# Input Format
# The first line contains the first integer, a, and the second line contains the second integer, b.

# Output Format
# Print the result as described above.

# Sample Input

# 177
# 10
# Sample Output

# 17
# 7
# (17, 7)

#-------------------------------------------------------------

# Görev
# İki tamsayıyı, a ve b'yi okuyun ve üç satır yazdırın.
# İlk satır a//b tamsayı bölümüdür (Python2 kullanırken bölümü __future__'den almayı unutmayın).
# İkinci satır modulo operatörünün sonucudur: a%b.
# Üçüncü satır a ve b'nin divmodunu yazdırır.

# Giriş Formatı
# İlk satır birinci tamsayıyı, a'yı, ikinci satır ise ikinci tamsayıyı, b'yi içerir.

# Çıkış formatı
# Sonucu yukarıda açıklandığı gibi yazdırın.

# Örnek Giriş

# 177
# 10
# Örnek Çıktı

# 17
# 7
# (17, 7)

# Enter your code here. Read input from STDIN. Print output to STDOUT

A = int(input())
B = int(input())

print(A//B)
print(A%B)
print(divmod(A, B))