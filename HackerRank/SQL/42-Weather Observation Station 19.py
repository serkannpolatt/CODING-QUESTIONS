# Problem
# Consider P1(a, c) and P2(b, d) to be two points on a 2D plane where (a, b) are the respective minimum and maximum values of Northern Latitude (LAT_N) and (c, d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

# Query the Euclidean Distance between points P1 and P2 and format your answer to display 4 decimal digits.

# Input Format
# The STATION table is described as follows:

# Field	Type
# ID	NUMBER
# CITY	VARCHAR2(21)
# STATE	VARCHAR2(2)
# LAT_N	NUMBER
# Long_W	NUMBER
# STATION
# where LAT_N is the northern latitude and LONG_W is the western longitude.

#-----------------------------------------

# Sorun
# P1(a, c) ve P2(b, d)'nin bir 2B düzlemde iki nokta olduğunu düşünün; burada (a, b) Kuzey Enlemi (LAT_N) ve (c, d)'nin ilgili minimum ve maksimum değerleridir. STATION'daki Batı Boylamının (LONG_W) ilgili minimum ve maksimum değerleri.

# P1 ve P2 noktaları arasındaki Öklid Mesafesini sorgulayın ve cevabınızı 4 ondalık basamak gösterecek şekilde biçimlendirin.

# Giriş Formatı
# İSTASYON tablosu şu şekilde açıklanmıştır:

# Alan türü
# KİMLİK NUMARASI
# ŞEHİR VARCHAR2(21)
# DEVLET VARCHAR2(2)
# LAT_N NUMBER
# Long_W NUMBER
# İSTASYON
# burada LAT_N kuzey enlemi ve LONG_W batı boylamıdır.

SELECT ROUND(SQRT(POWER(MAX(LAT_N)-MIN(LAT_N),2)+POWER(MAX(LONG_W)-MIN(LONG_W),2)),4)
FROM STATION;