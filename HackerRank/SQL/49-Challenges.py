# Problem
# Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

# Input Format
# The following tables contain challenge data:

# Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker. 
# Challenges: The challenge_id is the id of the challenge, and hacker_id is the id of the student who created the challenge. 
# Sample Input 0

# Hackers Table

# Challenges Table

# Sample Output 0

# 21283 Angela 6
# 88255 Patrick 5
# 96196 Lisa 1
# Sample Input 1


# Hackers Table

# Challenges Table

# Sample Output 1


# 12299 Rose 6
# 34856 Angela 6
# 79345 Frank 4
# 80491 Patrick 3
# 81041 Lisa 1
# Explanation
# For Sample Case 0, we can get the following details:

# Students 5077 and 62743 both created 4 challenges, but the maximum number of challenges created is 6 so these students are excluded from the result.

# For Sample Case 1, we can get the following details:

# Students 12299 and 34856 both created 6 challenges. Because 6 is the maximum number of challenges created, these students are included in the result.

#----------------------------------------------

# Sorun
# Julia, öğrencilerinden bazı kodlama zorlukları oluşturmalarını istedi. Hacker_id'yi, adı ve her öğrenci tarafından oluşturulan toplam mücadele sayısını yazdırmak için bir sorgu yazın. Sonuçlarınızı azalan düzende toplam zorluk sayısına göre sıralayın. Birden fazla öğrenci aynı sayıda zorluk oluşturduysa, sonucu hacker_id'ye göre sıralayın. Birden fazla öğrenci aynı sayıda zorluk oluşturduysa ve sayı oluşturulan maksimum zorluk sayısından azsa, bu öğrencileri sonuçtan hariç tutun.

# Giriş Formatı
# Aşağıdaki tablolar sorgulama verilerini içerir:

# Hacker'lar: hacker_id, bilgisayar korsanının kimliğidir ve ad, bilgisayar korsanının adıdır.
# Zorluklar: Challenge_id, meydan okumanın kimliğidir ve hacker_id, meydan okumayı oluşturan öğrencinin kimliğidir.
# Örnek Giriş 0

# Hacker Tablosu

# Zorluklar Tablosu

# Örnek Çıktı 0

# 21283 Angela 6
# 88255 Patrick 5
# 96196 Lisa 1
# Örnek Giriş 1


# Hacker Tablosu

# Zorluklar Tablosu

# Örnek Çıktı 1


# 12299 Gül 6
# 34856 Angela 6
# 79345 Frank 4
#80491 Patrick 3
# 81041 Lisa 1
# Açıklama
# Örnek Durum 0 için aşağıdaki ayrıntıları alabiliriz:

# 5077 ve 62743 numaralı öğrencilerin her ikisi de 4 zorluk oluşturdu, ancak oluşturulan maksimum zorluk sayısı 6'dır, dolayısıyla bu öğrenciler sonuçtan hariç tutulur.

# Örnek Durum 1 için aşağıdaki ayrıntıları alabiliriz:

# 12299 ve 34856 numaralı öğrencilerin her ikisi de 6 zorluk yarattı. 6, oluşturulan maksimum zorluk sayısı olduğundan, bu öğrenciler sonuca dahil edilir.



SELECT h.hacker_id, 
       h.name, 
       COUNT(c.challenge_id) AS c_count
FROM Hackers h
JOIN Challenges c ON c.hacker_id = h.hacker_id
GROUP BY h.hacker_id, h.name
HAVING c_count = 
    (SELECT COUNT(c2.challenge_id) AS c_max
     FROM challenges as c2 
     GROUP BY c2.hacker_id 
     ORDER BY c_max DESC limit 1)
OR c_count IN 
    (SELECT DISTINCT c_compare AS c_unique
     FROM (SELECT h2.hacker_id, 
                  h2.name, 
                  COUNT(challenge_id) AS c_compare
           FROM Hackers h2
           JOIN Challenges c ON c.hacker_id = h2.hacker_id
           GROUP BY h2.hacker_id, h2.name) counts
     GROUP BY c_compare
     HAVING COUNT(c_compare) = 1)

ORDER BY c_count DESC, h.hacker_id;