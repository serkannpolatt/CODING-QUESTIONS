# Task
# You are given two values a and b.

# Perform integer division and print a / b.

# Input Format
# The first line contains T, the number of test cases.


# The next T lines each contain the space separated values of a and b.

# Constraints
# 0 < T < 10

# Output Format
# Print the value of a / b.

# In the case of ZeroDivisionError or ValueError, print the error code.

#-------------------------------------------------------------

# Görev
# Size a ve b olmak üzere iki değer verilir.

# Tamsayı bölme işlemini gerçekleştirin ve a / b yazdırın.

# Giriş Formatı
# İlk satır, test senaryolarının sayısı olan T'yi içerir.


# Sonraki T satırlarının her biri, a ve b'nin boşlukla ayrılmış değerlerini içerir.

# Kısıtlamalar
# 0 < T < 10

# Çıkış formatı
# a / b değerini yazdırın.

# ZeroDivisionError veya ValueError durumunda hata kodunu yazdırın.

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)