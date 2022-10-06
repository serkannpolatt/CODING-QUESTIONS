# Problem
# Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
# The STATION table is described as follows:

# STATION

# Field	Type
# ID	NUMBER
# CITY	VARCHAR2(21)
# STATE	VARCHAR2(2)
# LAT_N	NUMBER
# LONG_W	NUMBER
# where LAT_N is the northern latitude and LONG_W is the western longitude.

# Sample Input

# For example, CITY has four entries: DEF, ABC, PQRS and WXY.

# Sample Output

# ABC 3
# PQRS 4
# Explanation
# When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths 3, 3, 4 and 3. The longest name is PQRS, but there are 3 options for shortest named city. Choose ABC, because it comes first alphabetically.


# Note
# You can write two separate queries to get the desired output. It need not be a single query.

#---------------------------------------------

# Sorun
# STATION'daki en kısa ve en uzun CITY adlarına sahip iki şehri ve bunların uzunluklarını (yani, addaki karakter sayısı) sorgulayın. Birden fazla en küçük veya en büyük şehir varsa, alfabetik olarak sıralandığında ilk gelen şehri seçin.
# İSTASYON tablosu şu şekilde açıklanmıştır:

# İSTASYON

# Alan türü
# KİMLİK NUMARASI
# ŞEHİR VARCHAR2(21)
# DEVLET VARCHAR2(2)
# LAT_N NUMBER
# LONG_W NUMBER
# burada LAT_N kuzey enlemi ve LONG_W batı boylamıdır.

# Örnek Giriş

# Örneğin, CITY'nin dört girişi vardır: DEF, ABC, PQRS ve WXY.

# Örnek Çıktı

# ABC 3
# PQRS 4
# Açıklama
# Alfabetik olarak sıralandığında ŞEHİR adları ABC, DEF, PQRS ve WXY olarak 3, 3, 4 ve 3 uzunluklarında listelenir. En uzun isim PQRS'dir, ancak en kısa isim verilen şehir için 3 seçenek vardır. ABC'yi seçin, çünkü alfabetik olarak önce gelir.


# Not
# İstenilen çıktıyı almak için iki ayrı sorgu yazabilirsiniz. Tek bir sorgu olması gerekmez.

select city c, length(city) l
from   station
order by l desc, c asc
limit 1;

select city c, length(city) l
from   station
order by l asc, c asc
limit 1;