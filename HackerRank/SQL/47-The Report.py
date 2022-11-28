# Problem
# You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.

# Column	Type
# ID	Integer
# Name	String
# Marks	Integer
# Grades contains the following data:

# Grade	Min_Mark	Max_Mark
# 1	0	9
# 2	10	19
# 3	20	29
# 4	30	39
# 5	40	49
# 6	50	59
# 7	60	69
# 8	70	79
# 9	80	89
# 10	90	99
# Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn’t want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade — i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use “NULL” as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

# Write a query to help Eve.

# Sample Input

# Id	Name	Marks
# 1	Julia	88
# 2	Samantha	68
# 3	Maria	99
# 4	Scarlet	78
# 5	Ashley	63
# 6	Jane	81
# Sample Output

# Maria 10 99
# Jane 9 81
# Julia 9 88 
# Scarlet 8 78
# NULL 7 63
# NULL 7 68
# Note

# Print “NULL”  as the name if the grade is less than 8.

# Explanation
# Consider the following table with the grades assigned to the students:

# Id	Name	Marks	Grade
# 1	Julia	88	9
# 2	Samantha	68	7
# 3	Maria	99	10
# 4	Scarlet	78	8
# 5	Ashley	63	7
# 6	Jane	81	9
# So, the following students got 8, 9 or 10 grades:

# Maria (grade 10)
# Jane (grade 9)
# Julia (grade 9)
# Scarlet (grade 8)

#------------------------------------

# Sorun
# Size iki tablo verilir: Öğrenciler ve Notlar. Öğrenciler, Kimlik, Ad ve İşaretler olmak üzere üç sütun içerir.

# Sütun Türü
# Kimlik Tam Sayısı
# İsim Dizesi
# İşaretler Tamsayı
# Notlar aşağıdaki verileri içerir:

# Not Min_Mark Max_Mark
# 1 0 9
# 2 10 19
# 3 20 29
# 4 30 39
# 5 40 49
# 6 50 59
# 7 60 69
# 8 70 79
# 9 80 89
# 10 90 99
# Ketty, Eve'e üç sütun içeren bir rapor oluşturma görevi verir: Ad, Derece ve İşaret. Ketty, 8'den daha düşük not alan öğrencilerin İSİMLERİNİ istemez. Rapor, nota göre azalan sırada olmalıdır - yani daha yüksek notlar önce girilir. Aynı sınıftan (8-10) birden fazla öğrenci varsa, bu öğrencileri adlarına göre alfabetik olarak sıralayınız. Son olarak, not 8'den düşükse, isim olarak “NULL” kullanın ve notlarına göre azalan sırayla listeleyin. Aynı nota (1-7) atanan birden fazla öğrenci varsa, bu öğrencileri notlarına göre artan sırada sıralayın.

# Eve'e yardım etmek için bir sorgu yaz.

# Örnek Giriş

# Kimlik Adı İşaretleri
# 1 Julia 88
# 2 Samantha 68
# 3 Maria 99
# 4 Kızıl 78
# 5 Ashley 63
# 6 Jane 81
# Örnek Çıktı

# Maria 10 99
# Jane 9 81
# Julia 9 88
# Kızıl 8 78
# NULL 7 63
# NULL 7 68
# Not

# Not 8'den küçükse isim olarak “NULL” yazdırın.

# Açıklama
# Öğrencilere verilen notlarla birlikte aşağıdaki tabloyu inceleyin:

# Kimlik Adı İşaretleri Notu
# 1 Julia 88 9
# 2 Samantha 68 7
# 3 Maria 99 10
# 4 Kızıl 78 8
# 5 Ashley 63 7
# 6 Jane 81 9
# Böylece, aşağıdaki öğrenciler 8, 9 veya 10 not aldı:

# Maria (10. sınıf)
# Jane (9. sınıf)
# Julia (9. sınıf)
# Scarlet (8. sınıf)

SELECT CASE
    WHEN G.grade > 7 THEN S.name
    ELSE NULL
    end AS names,
    G.grade,
    S.marks
FROM   students S
    JOIN grades G
    ON S.marks BETWEEN G.min_mark AND G.max_mark
ORDER  BY G.grade DESC,
    names ASC,
    S.marks ASC;