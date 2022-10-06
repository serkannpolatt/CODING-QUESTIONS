# Problem
# Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

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
# STATION'dan sesli harflerle (a, e, i, o, u) biten ŞEHİR adlarının listesini sorgulayın. Sonucunuz kopyaları içeremez.

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
where city like '%a'
or
city like '%e'
or
city like '%i'
or
city like '%o'
or
city like '%u';