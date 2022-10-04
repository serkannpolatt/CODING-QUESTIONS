# Problem
# Query a list of CITY and STATE from the STATION table.
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
# STATION tablosundan CITY ve STATE listesini sorgulayın.
# İSTASYON tablosu şu şekilde açıklanmıştır:

# İSTASYON

# Alan türü
# KİMLİK NUMARASI
# ŞEHİR VARCHAR2(21)
# DEVLET VARCHAR2(2)
# LAT_N NUMBER
# LONG_W NUMBER
# burada LAT_N kuzey enlemi ve LONG_W batı boylamıdır.

SELECT CITY, STATE FROM STATION;