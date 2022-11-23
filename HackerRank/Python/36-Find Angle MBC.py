# Task
# ABC is a right triangle, 90o at B.
# Therefore, angle ABC = 90o.
# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and BC.
# Your task is to find angle MBC in degrees.

# Input Format
# The first line contains the length of side AB.
# The second line contains the length of side BC.

# Constraints
# 0 < AB <= 100
# 0 < BC <= 100
# Lengths AB and BC are natural numbers.
# Output Format
# Output angle MBC in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.

# Sample Input


# 10
# 10
# Sample Output

# 45°

#-------------------------------------------------------------

# Görev
# ABC, B'de 90o olan bir dik üçgendir.
# Buna göre ABC açısı = 90o.
# M noktası, AC hipotenüsünün orta noktasıdır.

# Size AB ve BC uzunlukları verildi.
# Senin görevin derece cinsinden MBC açısını bulmak.

# Giriş Formatı
# İlk satır AB kenarının uzunluğunu içerir.
# İkinci satır BC kenarının uzunluğunu içerir.

# Kısıtlamalar
# 0 < AB <= 100
# 0 < M.Ö. <= 100
# AB ve BC uzunlukları doğal sayılardır.
# Çıkış formatı
# Derece olarak MBC çıkış açısı.

# Not: Açıyı en yakın tam sayıya yuvarlayın.

# Örnekler:
# Açı 56.500001° ise, 57° çıktı alın.
# Açı 56.5000000° ise, 57° çıktı alın.
# Açı 56.4999999° ise, çıktı 56°.

# Örnek Giriş


# 10
# 10
# Örnek Çıktı

# 45°


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab=int(input())
bc=int(input())

ca=math.hypot(ab,bc)
mc=ca/2
bca=math.asin(1*ab/ca)
bm=math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca)))
mbc=math.asin(math.sin(bca)*mc/bm)

print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')