# Task
# Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

# The CITY table is described as follows:

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER

#---------------------------------------------

# Görev
# 120000'den büyük nüfusa sahip CITY tablosundaki tüm Amerikan şehirleri için NAME alanını sorgulayın. Amerika için Ülke Kodu ABD'dir.

# CITY tablosu şu şekilde açıklanmıştır:

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI

select name from city 
where countrycode = 'USA'
and population > 120000