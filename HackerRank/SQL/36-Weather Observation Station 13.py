# Problem
# Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.

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

#------------------------------------------------------------

# Sorun
# STATION'dan 38.7880'den büyük ve 137.2345'ten küçük değerlere sahip Kuzey Enlemlerinin (LAT_N) toplamını sorgulayın. Cevabınızı 4 ondalık basamağa kısaltın.

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

select round(sum(lat_n), 4) from station 
where lat_n > 38.7880 and lat_n < 137.2345;