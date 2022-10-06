# Problem
# Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

# Input Format
# The STATION table is described as follows:

# Field	Type
# ID	NUMBER
# CITY	VARCHAR2(21)
# STATE	VARCHAR2(2)
# LAT_N	NUMBER
# LONG_W	NUMBER
# where LAT_N is the northern latitude and LONG_W is the western longitude.

#---------------------------------------------

# Sorun
# STATION'dan sesli harflerle (yani, a, e, i, o veya u) başlayan ŞEHİR adlarının listesini sorgulayın. Sonucunuz kopyaları içeremez.

# Giriş Formatı
# İSTASYON tablosu şu şekilde açıklanmıştır:

# Alan türü
# KİMLİK NUMARASI
# ŞEHİR VARCHAR2(21)
# DEVLET VARCHAR2(2)
# LAT_N NUMBER
# LONG_W NUMBER
# burada LAT_N kuzey enlemi ve LONG_W batı boylamıdır.


SELECT DISTINCT city FROM station WHERE city LIKE "A%" OR city LIKE "E%" OR city LIKE "I%" OR city LIKE "O%" OR city LIKE "U%";