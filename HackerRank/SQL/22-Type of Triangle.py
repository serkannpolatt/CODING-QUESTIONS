# Problem
# Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

# Equilateral: It’s a triangle with 3 sides of equal length.
# Isosceles: It’s a triangle with 2 sides of equal length.
# Scalene: It’s a triangle with 3 sides of differing lengths.
# Not A Triangle: The given values of A, B, and C don’t form a triangle.
# Input Format
# The TRIANGLES table is described as follows:

# Column	Type
# A	Integer
# B	Integer
# C	Integer
# Each row in the table denotes the lengths of each of a triangle’s three sides.

# Sample Input

# A	B	C
# 20	20	23
# 20	20	20
# 20	21	22
# 13	14	30
# Sample Output

# Isosceles
# Equilateral
# Scalene
# Not A Triangle
# Explanation
# Values in the tuple (20, 20, 30) form an Isosceles triangle, because A == B.
# Values in the tuple (20, 20, 20) form an Equilateral triangle, because A == B == C. Values in the tuple (20, 21, 22) form a Scalene triangle, because A =! B =! C.
# Values in the tuple (13, 14, 30) cannot form a triangle because the combined value of sides A and B is not larger than that of side C.

#------------------------------------------------------------

# Sorun
# Üç kenar uzunluğunu kullanarak TRIANGLES tablosundaki her kaydın türünü tanımlayan bir sorgu yazın. Tablodaki her kayıt için aşağıdaki ifadelerden birinin çıktısını alın:

# Eşkenar: 3 kenarı eşit uzunlukta olan üçgendir.
# İkizkenar: 2 kenarı eşit uzunlukta olan üçgendir.
# Scalene: 3 kenarı farklı uzunluklarda olan bir üçgendir.
# Üçgen Değil: Verilen A, B ve C değerleri üçgen oluşturmaz.
# Giriş Formatı
# TRIANGLES tablosu şu şekilde açıklanmıştır:

# Sütun Türü
# Bir Tam Sayı
# B Tamsayı
# C Tamsayı
# Tablodaki her satır, bir üçgenin üç kenarının her birinin uzunluklarını gösterir.

# Örnek Giriş

# A B C
# 20 20 23
# 20 20 20
# 20 21 22
# 13 14 30
# Örnek Çıktı

# ikizkenar
# eşkenar
# Scalene
# Üçgen Değil
# Açıklama
# Gruptaki (20, 20, 30) değerler bir İkizkenar üçgen oluşturur, çünkü A == B.
# Gruptaki (20, 20, 20) değerler bir Eşkenar üçgen oluşturur, çünkü A == B == C. Gruptaki (20, 21, 22) değerler bir Scalene üçgeni oluşturur, çünkü A =! B =! C.
# Gruptaki (13, 14, 30) değerler bir üçgen oluşturamaz çünkü A ve B kenarlarının birleşik değeri C kenarından daha büyük değildir.


select if(A+B<=C or B+C<=A or A+C<=B,"Not A Triangle",
if(A=B and B=C,"Equilateral",
if(A=B or B=C or A=C,"Isosceles","Scalene")))
from TRIANGLES as T;