# Problem
# You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one, too!

# The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of 0 from your result.

# Input Format
# The following tables contain contest data:

# Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker. 
# Submissions: The submission_id is the id of the submission, hacker_id is the id of the hacker who made the submission, challenge_id is the id of the challenge for which the submission belongs to, and score is the score of the submission. 
# Sample Input

# Hackers Table: 

# Submissions Table:

# Sample Output


# 4071 Rose 191
# 74842 Lisa 174
# 84072 Bonnie 100
# 4806 Angela 89
# 26071 Frank 85
# 80305 Kimberly 67
# 49438 Patrick 43
# Explanation
# Hacker 4071 submitted solutions for challenges 19797 and 49593, so the total score = 95 + max(43, 96) = 191.

# Hacker 74842 submitted solutions for challenges 19797 and 63132, so the total score = max(98, 5) +76 = 174

# Hacker 84072 submitted solutions for challenges 49593 and 63132, so the total score = 100 + 0 = 100.


# The total scores for hackers 4806, 26071, 80305, and 49438 can be similarly calculated.

#-------------------------------------------

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


select h.hacker_id,h.name,sum(sscore)
from Hackers h inner join (select s.hacker_id,max(score) as sscore from Submissions s group by s.hacker_id,s.challenge_id) st on h.hacker_id=st.hacker_id
group by h.hacker_id,h.name
having sum(sscore)>0
order by sum(sscore) desc,h.hacker_id asc;