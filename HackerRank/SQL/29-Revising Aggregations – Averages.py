# Problem
# Query the average population of all cities in CITY where District is California.

# Input Format
# The CITY is described as follows:

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER

#------------------------------------------------------------

# Sorun
# District'in California olduğu CITY şehrinde bulunan tüm şehirlerin ortalama nüfusunu sorgulayın.

# Giriş Formatı
# ŞEHİR şu şekilde tanımlanır:

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI

select avg(population) from city where district='California';