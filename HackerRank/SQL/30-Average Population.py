# Problem
# Query the average population for all cities in CITY, rounded down to the nearest integer.

# Input Format
# The CITY is described as follows:

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER

#---------------------------------------------------------

# Sorun
# CITY'deki tüm şehirler için en yakın tam sayıya yuvarlanmış ortalama nüfusu sorgulayın.

# Giriş Formatı
# ŞEHİR şu şekilde tanımlanır:

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI

select floor(avg(population)) from city;