# Problem
# Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

# Input Format
# The CITY table is described as follows:

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER

#--------------------------------------------------------------

# Sorun
# CITY'deki tüm Japon şehirlerinin nüfuslarının toplamını sorgula. Japonya için COUNTRYCODE JPN'dir.

# Giriş Formatı
# CITY tablosu şu şekilde açıklanmıştır:

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI

select sum(population) from city where countrycode='JPN';