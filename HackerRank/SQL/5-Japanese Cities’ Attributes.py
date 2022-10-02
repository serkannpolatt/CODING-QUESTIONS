# Problem
# Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

# The CITY table is described as follows:

# CITY

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER

#---------------------------------------------

# Sorun
# CITY tablosundaki her Japon şehrinin tüm özelliklerini sorgulayın. Japonya için COUNTRYCODE JPN'dir.

# CITY tablosu şu şekilde açıklanmıştır:

# KENT

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI


SELECT * FROM CITY WHERE COUNTRYCODE = "JPN";