# Task
# The included code stub will read an integer, n, from STDIN.

# Without using any strings methods, try to print the following:

# 123……..n

# Note that “…..” represents the consecutive values in between.

# Example

# n = 5
# Print the string 12345.

# Input Format
# The first line contains an integer n.


# Constraints
# 1 ≤ n ≤ 150

# Output Format
# Print the list of integers from 1 through n as a string, without spaces.

#---------------------------------------------------

# Görev
# Dahil edilen kod saplaması, STDIN'den bir tamsayı, n okuyacaktır.

# Herhangi bir string yöntemi kullanmadan aşağıdakileri yazdırmayı deneyin:

# 123……..n

# “…..”nin aradaki ardışık değerleri temsil ettiğini unutmayın.

# Örnek

# n = 5
# 12345 dizesini yazdırın.

# Giriş Formatı
# İlk satır bir n tamsayısını içerir.


# Kısıtlamalar
# 1 ≤ n ≤ 150

# Çıkış formatı
# 1'den n'ye kadar tam sayıların listesini boşluk bırakmadan bir dize olarak yazdırın.


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")