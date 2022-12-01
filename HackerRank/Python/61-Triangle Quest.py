# Task
# You are given a positive integer N. Print a numerical triangle of height N – 1 like the one below:

# 1
# 22
# 333
# 4444
# 55555
# ......
# Can you do it using only arithmetic operations, a single for loop and print statement?

# Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

# Note: Using anything related to strings will give a score of 0.

# Input Format
# A single line containing integer, N.

# Constraints
# 1 <= N <= 9
# Output Format
# Print N – 1 lines as explained above.

# Sample Input


# 5
# Sample Output

# 1
# 22
# 333
# 4444

#-------------------------------------------------------------

# Görev
# Size pozitif bir N tamsayısı verildi. Aşağıdaki gibi N – 1 yüksekliğinde sayısal bir üçgen yazdırın:

# 1
# 22
# 333
# 4444
# 55555
# ......
# Sadece aritmetik işlemler, tek bir for döngüsü ve print deyimi kullanarak yapabilir misiniz?

# En fazla iki satır kullanın. İlk satır (for ifadesi) zaten sizin için yazılmıştır. Print deyimini tamamlamanız gerekir.

# Not: Dizelerle ilgili herhangi bir şey kullanmak 0 puan verecektir.

# Giriş Formatı
# N tamsayısını içeren tek bir satır.

# Kısıtlamalar
# 1 <= N <= 9
# Çıkış formatı
# Yukarıda açıklandığı gibi N – 1 satır yazdırın.

# Örnek Giriş


# 5
# Örnek Çıktı

# 1
# 22
# 333
# 4444


for i in range(1, int(input())):
    print((10**(i)//9)*i)