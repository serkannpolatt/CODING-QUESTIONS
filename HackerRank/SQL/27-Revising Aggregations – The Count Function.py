# Problem
# Query a count of the number of cities in CITY having a Population larger than 100,000.

# Input Format
# The CITY table is described as follows:

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER
# CITY
# Solution – Revising Aggregations – The Count Function in SQL

#------------------------------------------------------------

# Sorun
# CITY'de Nüfusu 100.000'den fazla olan şehirlerin sayısını sorgulayın.

# Giriş Formatı
# CITY tablosu şu şekilde açıklanmıştır:

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI
# KENT
# Çözüm – Toplamaları Gözden Geçirme – SQL'de Sayım İşlevi

SELECT COUNT(*) FROM CITY WHERE POPULATION > 100000