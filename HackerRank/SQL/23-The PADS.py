# Problem
# Generate the following two result sets:

# Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
# Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:
# There are a total of [occupation_count] [occupation]s.
# where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.

# Note: There will be at least two entries in the table for each type of occupation.

# Input Format
# Column	Type
# Name	String
# Occupation	String
# The OCCUPATIONS table is described as follows: 

# Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.

# Sample Input

# An OCCUPATIONS table that contains the following records:


# Name	Occupation
# Samantha	Doctor
# Julia	Actor
# Maria	Actor
# Meera	Singer
# Ashley	Professor
# Ketty	Professor
# Christeen	Professor
# Jane	Actor
# Jenny	Doctor
# Priya	Singer
# Sample Output

# Ashely(P)
# Christeen(P)
# Jane(A)
# Jenny(D)
# Julia(A)
# Ketty(P)
# Maria(A)
# Meera(S)
# Priya(S)
# Samantha(D)
# There are a total of 2 doctors.
# There are a total of 2 singers.
# There are a total of 3 actors.
# There are a total of 3 professors.
# Explanation

# The results of the first query are formatted to the problem description’s specifications.
# The results of the second query are ascendingly ordered first by number of names corresponding to each profession (2 <= 2 <= 3 <= 3), and then alphabetically by profession (doctor <= singer, and actor <= professor).

#------------------------------------------------------------

# Sorun
# Aşağıdaki iki sonuç kümesini oluşturun:

# MESLEKLER içindeki tüm isimlerin alfabetik olarak sıralanmış bir listesini, hemen ardından her mesleğin ilk harfini parantez içinde (yani: parantez içine alınmış) sorgulayın. Örneğin: AnActorName(A), ADoctorName(D), AProfessorName(P) ve ASingerName(S).
# MESLEKLER'deki her mesleğin tekrarlanma sayısını sorgulayın. Olayları artan düzende sıralayın ve aşağıdaki biçimde çıktısını alın:
# Toplam [işgal_sayısı] [işgal] var.
# burada [meslek_sayısı], MESLEKLER içindeki bir mesleğin oluşum sayısıdır ve [meslek] küçük harfli meslek adıdır. Birden fazla Meslek aynı [meslek_sayısı]'na sahipse, bunlar alfabetik olarak sıralanmalıdır.

# Not: Her meslek türü için tabloda en az iki giriş olacaktır.

# Giriş Formatı
# Sütun Türü
# İsim Dizesi
# Meslek Dizisi
# MESLEKLER tablosu şu şekilde açıklanmıştır:

# Meslek, şu değerlerden yalnızca birini içerecektir: Doktor, Profesör, Şarkıcı veya Aktör.

# Örnek Giriş

# Aşağıdaki kayıtları içeren bir MESLEK tablosu:


# İsim Meslek
# Samantha Doktor
# Julia Oyuncu
# Maria Oyuncu
# Meera Şarkıcısı
# Ashley Profesör
# Ketty Profesörü
# Hıristiyan Profesör
# Jane Aktör
#Jenny Doktor
# Priya Şarkıcı
# Örnek Çıktı

# Ashely(P)
# Christen(P)
# Jane(A)
#Jenny(D)
# Julia(A)
# Ketty(P)
# Maria(A)
# Meera(lar)
# Priya(lar)
# Samantha(D)
# Toplam 2 doktor var.
# Toplam 2 şarkıcı var.
# Toplam 3 oyuncu var.
# Toplam 3 profesör var.
# Açıklama

# İlk sorgunun sonuçları, sorun açıklamasının özelliklerine göre biçimlendirilir.
# İkinci sorgunun sonuçları, önce her mesleğe karşılık gelen isim sayısına göre (2 <= 2 <= 3 <= 3) ve daha sonra mesleğe göre alfabetik olarak (doktor <= şarkıcı ve aktör <= profesör) artan şekilde sıralanır.

SELECT concat(NAME,concat("(",concat(substr(OCCUPATION,1,1),")"))) FROM OCCUPATIONS ORDER BY NAME ASC;
SELECT "There are a total of ", count(OCCUPATION), concat(lower(occupation),"s.") FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY count(OCCUPATION), OCCUPATION ASC