# Problem
# Given an integer, n, print the following values for each integer i from 1 to n:

# Decimal 
# Octal 
# Hexadecimal (capitalized)
# Binary
# The four values must be printed on a single line in the order specified above for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.

# Input Format
# A single integer denoting n.

# Constraints
# 1 <= n <= 99

# Output Format
# Print n lines where each line i (in the range 1 <= i <= n ) contains the respective decimal, octal, capitalized hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.

#----------------------------------------------------------

# Sorun
# Bir n tamsayısı verildiğinde, 1'den n'ye kadar olan her i tamsayı için aşağıdaki değerleri yazdırın:

# Ondalık
# Sekizli
# Onaltılık (büyük harfle)
# İkili
# Dört değer, 1'den n'ye kadar her i için yukarıda belirtilen sırayla tek bir satıra yazdırılmalıdır. Her değer, n'nin ikili değerinin genişliğiyle eşleşmesi için boşlukla doldurulmalıdır.

# Giriş Formatı
# n'yi gösteren tek bir tam sayı.

# Kısıtlamalar
# 1 <= n <= 99

# Çıkış formatı
# Her i satırının (1 <= i <= n aralığında) i'nin ilgili ondalık, sekizlik, büyük harfli onaltılık ve ikili değerlerini içerdiği n satır yazdırın. Yazdırılan her değer, n'nin ikili değerinin genişliğine göre biçimlendirilmelidir.

def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]

        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)