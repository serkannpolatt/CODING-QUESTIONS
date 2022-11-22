# Problem
# Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to 4 decimal places.

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

#---------------------------------------------------------------

# Sorun
# 137.2345'ten küçük olan STATION'daki en büyük Kuzey Enlemi (LAT_N) için Batı Boylamı'nı (LONG_W) sorgulayın. Cevabınızı 4 ondalık basamağa yuvarlayın.

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

select round(long_w, 4) from station 
where lat_n = (select max(lat_n) 
from station where lat_n < 137.2345);