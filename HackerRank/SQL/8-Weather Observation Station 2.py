# Problem
# Query the following two values from the STATION table:

# The sum of all values in LAT_N rounded to a scale of 2 decimal places.
# The sum of all values in LONG_W rounded to a scale of 2 decimal places.
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

# Output Format
# Your results must be in the form:

# lat lon
# where lat is the sum of all values in LAT_N and lon is the sum of all values in LONG_W. Both results must be rounded to a scale of 2 decimal places.

#---------------------------------------------

# Sorun
# STATION tablosundan aşağıdaki iki değeri sorgulayın:

# LAT_N'deki tüm değerlerin toplamı 2 ondalık basamaklı bir ölçeğe yuvarlanır.
# LONG_W içindeki tüm değerlerin toplamı 2 ondalık basamaklı bir ölçeğe yuvarlanır.
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

# Çıkış formatı
# Sonuçlarınız şu şekilde olmalıdır:

# enlem
# burada lat, LAT_N'deki tüm değerlerin toplamıdır ve lon, LONG_W'deki tüm değerlerin toplamıdır. Her iki sonuç da 2 ondalık basamaklı bir ölçeğe yuvarlanmalıdır.

select round(sum(lat_n), 2), round(sum(long_w), 2) 
from station;