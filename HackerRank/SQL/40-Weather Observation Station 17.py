# Problem
# Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places.

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

#--------------------------------------------------

# Sorun
# STATION'daki en küçük Kuzey Enleminin (LAT_N) 38.7780'den büyük olduğu Batı Boylamını (LONG_W) sorgulayın. Cevabınızı 4 ondalık basamağa yuvarlayın.

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
where lat_n = (select min(lat_n) 
from station where lat_n > 38.7780);