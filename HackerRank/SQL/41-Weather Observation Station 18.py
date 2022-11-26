# Problem
# Consider P1(a, b) and P2(c, d) to be two points on a 2D plane.

# a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
# b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
# c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
# d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
# Query the Manhattan Distance between points P1 and P2 and round it to a scale of  decimal places.

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
# P1(a, b) ve P2(c, d)'yi 2B düzlemde iki nokta olarak kabul edin.

# a, Kuzey Enlemindeki minimum değere eşit olur (İSTASYON'da LAT_N).
# b, Batı Boylamındaki minimum değere eşit olur (İSTASYON'da LONG_W).
# c, Kuzey Latitude'daki maksimum değere eşit olur (İSTASYON'da LAT_N).
# d, Batı Boylamındaki maksimum değere eşit olur (İSTASYON'da LONG_W).
# P1 ve P2 noktaları arasındaki Manhattan Mesafesini sorgulayın ve bunu bir ondalık basamak ölçeğine yuvarlayın.

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


select Round(ABS(MIN(LAT_N) - MAX(LAT_N)) + ABS(MIN(LONG_W) - MAX(LONG_W)),4)
FROM STATION;