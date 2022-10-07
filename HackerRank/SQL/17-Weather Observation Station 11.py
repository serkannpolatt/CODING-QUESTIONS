# Problem
# Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

# Input Format
# The STATION table is described as follows:

# STATION

# Field	Type
# ID	NUMBER
# CITY	VARCHAR2(21)
# STATE	VARCHAR2(2)
# LAT_N	NUMBER
# LONG_W	NUMBER
# where LAT_N is the northern latitude and LONG_W is the western longitude.

#---------------------------------------------

# Sorun
# STATION'dan sesli harfle başlamayan veya sesli harfle bitmeyen ŞEHİR adları listesini sorgulayın. Sonucunuz kopyaları içeremez.

# Giriş Formatı
# İSTASYON tablosu şu şekilde açıklanmıştır:

# İSTASYON

# Alan türü
# KİMLİK NUMARASI
# ŞEHİR VARCHAR2(21)
# DEVLET VARCHAR2(2)
# LAT_N NUMBER
# LONG_W NUMBER
# burada LAT_N kuzey enlemi ve LONG_W batı boylamıdır.

select distinct city
from station 
where not (city like 'A%' or city like 'E%' or city like 'I%' or city like 'O%' or  city like 'U%') or not (city like '%a' or city like '%e' or city like '%i' or city like '%o' or  city like '%u');