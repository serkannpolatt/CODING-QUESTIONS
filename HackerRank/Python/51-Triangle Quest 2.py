# Task
# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:

# 1
# 121
# 12321
# 1234321
# 123454321
# You can’t take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.

# Note:
# Using anything related to strings will give a score of 0.
# Using more than one for-statement will give a score of 0.

# Input Format
# A single line of input containing the integer N.

# Constraints
# 0 < N < 10
# Output Format
# Print the palindromic triangle of size N as explained above.

# Sample Input

# 5
# Sample Output

# 1
# 121
# 12321
# 1234321
# 123454321

#-------------------------------------------------------------

# Görev
# Size pozitif bir N tamsayısı verildi.
# Göreviniz N boyutunda bir palindromik üçgen basmak.

# Örneğin, boyutu 5 olan bir palindromik üçgen:

# 1
# 121
# 12321
# 1234321
#123454321
# İkiden fazla satır alamazsınız. İlk satır (bir for-ifadesi) zaten sizin için yazılmıştır.
# Tam olarak bir print deyimi kullanarak kodu tamamlamanız gerekiyor.

# Not:
# Dizelerle ilgili herhangi bir şey kullanmak 0 puan verecektir.
# Birden fazla for ifadesi kullanmak 0 puan verecektir.

# Giriş Formatı
# N tamsayısını içeren tek bir girdi satırı.

# Kısıtlamalar
# 0 < N < 10
# Çıkış formatı
# N boyutundaki palindromik üçgeni yukarıda açıklandığı gibi yazdırın.

# Örnek Giriş

# 5
# Örnek Çıktı

# 1
# 121
# 12321
# 1234321
#123454321

for i in range(1, int(input())+1):
    print(((10**i)//9)**2)