# Problem
# Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

# Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

# Input Format
# The CITY and COUNTRY tables are described as follows:

# Field	Type
# ID	NUMBER
# NAME	VARCHAR2(17)
# COUNTRYCODE	VARCHAR2(3)
# DISTRICT	VARCHAR2(20)
# POPULATION	NUMBER
# CITY
# Field	Type
# CODE	VARCHAR2(3)
# NAME	VARCHAR2(44)
# CONTINENT	VARCHAR2(13)
# REGION	VARCHAR2(25)
# SURFACEAREA	NUMBER
# INDEPYEAR	VARCHAR2(5)
# POPULATION	NUMBER
# LIFEEXPECTANCY	VARCHAR2(4)
# GNP	NUMBER
# GNPOLD	VARCHAR2(9)
# LOCALNAME	VARCHAR2(44)
# GOVERNMENTFORM	VARCHAR2(44)
# HEADOFSTATE	VARCHAR2(32)
# CAPITAL	VARCHAR2(4)
# CODE2	VARCHAR2(2)

#------------------------------

# Sorun
# CITY ve COUNTRY tabloları verildiğinde, tüm kıtaların adlarını (COUNTRY.Continent) ve ilgili ortalama şehir nüfuslarını (CITY.Population) en yakın tam sayıya yuvarlayarak sorgulayın.

# Not: CITY.CountryCode ve COUNTRY.Code eşleşen anahtar sütunlardır.

# Giriş Formatı
# ŞEHİR ve ÜLKE tabloları şu şekilde açıklanmıştır:

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI
# KENT
# Alan türü
# KOD VARCHAR2(3)
# İSİM VARCHAR2(44)
# Kıta VARCHAR2(13)
# BÖLGE VARCHAR2(25)
# YÜZEYALAN NUMARASI
# INDEPYEAR VARCHAR2(5)
# NÜFUS SAYISI
# YAŞAM BEKLENTİ VARCHAR2(4)
# GSMH SAYISI
# GNPOLD VARCHAR2(9)
# YEREL AD VARCHAR2(44)
# GOVERNMENTFORM VARCHAR2(44)
# HEADOFSTATE VARCHAR2(32)
# SERMAYE VARCHAR2(4)
# CODE2 VARCHAR2(2)

select country.continent, floor(avg(city.population))
from country
join city on city.countrycode = country.code
group by country.continent;