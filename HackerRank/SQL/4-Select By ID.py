# Problem
# Query all columns for a city in CITY with the ID 1661.

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
# 1661 kimliğine sahip CITY içindeki bir şehrin tüm sütunlarını sorgula.

# CITY tablosu şu şekilde açıklanmıştır:

# KENT

# Alan türü
# KİMLİK NUMARASI
# İSİM VARCHAR2(17)
# COUNTRYCODE VARCHAR2(3)
# BÖLGE VARCHAR2(20)
# NÜFUS SAYISI


SELECT * FROM CITY WHERE ID = 1661;