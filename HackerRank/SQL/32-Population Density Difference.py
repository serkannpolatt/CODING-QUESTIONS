# Problem
# Query the difference between the maximum and minimum populations in CITY.

# Input Format
# The CITY table is described as follows:

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER

#-----------------------------------------------

# Sorun
# CITY'deki maksimum ve minimum popülasyonlar arasındaki farkı sorgulayın.

# Giriş Formatı
# CITY tablosu şu şekilde açıklanmıştır:

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI

select max(population) - min(population) from city;