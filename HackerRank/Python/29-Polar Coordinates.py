# # Task
# # You are given a complex z. Your task is to convert it to polar coordinates.

# # Input Format
# # A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.

# # Constraints
# # Given number is a valid complex number.

# # Output Format
# # Output two lines:

# # The first line should contain the value of r.

# # The second line should contain the value of q.

# #---------------------------------------------------

# Görev
# Size karmaşık bir z verilir. Senin görevin onu kutupsal koordinatlara dönüştürmek.

# Giriş Formatı
# Karmaşık z sayısını içeren tek bir satır. Not: karmaşık () işlevi, girişi karmaşık bir sayıya dönüştürmek için python'da kullanılabilir.

# kısıtlamalar
# Verilen sayı geçerli bir karmaşık sayıdır.

# Çıkış formatı
# Çıktı iki satır:

# İlk satır r değerini içermelidir.

# İkinci satır q değerini içermelidir.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
n = input()
print(abs(complex(n)))
print(cmath.phase(complex(n)))