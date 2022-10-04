# Problem
# Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
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
# ŞEHİR tablosundaki tüm Japon şehirlerinin adlarını sorgulayın. Japonya için COUNTRYCODE JPN'dir.
# CITY tablosu şu şekilde açıklanmıştır:

# KENT

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI

SELECT NAME FROM CITY WHERE COUNTRYCODE = "JPN";