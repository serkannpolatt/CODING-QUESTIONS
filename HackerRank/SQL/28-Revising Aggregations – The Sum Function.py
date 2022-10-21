# Problem
# Query the total population of all cities in CITY where District is California.

# Input Format
# The CITY table is described as follows:

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER

#------------------------------------------------------------

# Sorun
# District'in California olduğu CITY'deki tüm şehirlerin toplam nüfusunu sorgulayın.

# Giriş Formatı
# CITY tablosu şu şekilde açıklanmıştır:

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI

select sum(population)
from city
where district ='California';