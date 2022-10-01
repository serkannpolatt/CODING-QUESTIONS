# Task
# Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

# The CITY table is described as follows:

# CITY

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER

#---------------------------------------------

# Görev
# 100.000'den fazla nüfusa sahip CITY tablosundaki tüm Amerikan şehirleri için tüm sütunları sorgulayın. Amerika için Ülke Kodu ABD'dir.

# CITY tablosu şu şekilde açıklanmıştır:

# KENT

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI



SELECT * FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;