#     Problem
# Harry Potter and his friends are at Ollivander’s with Ron, finally replacing Charlie’s old broken wand.

# Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron’s interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.

# Input Format
# The following tables contain data on the wands in Ollivander’s inventory:

# Wands: The id is the id of the wand, code is the code of the wand, coins_needed is the total number of gold galleons needed to buy the wand, and power denotes the quality of the wand (the higher the power, the better the wand is).
# Wands_Property: The code is the code of the wand, age is the age of the wand, and is_evil denotes whether the wand is good for the dark arts. If the value of is_evil is 0, it means that the wand is not evil. The mapping between code and age is one-one, meaning that if there are two pairs, (code1, age1) and (code2, age2), then code1 != code2 and age1 != age2.
# Sample Input

# Wands Table

# Wands_Property Table:

# Sample Output


# 9 45 1647 10
# 12 17 9897 10
# 1 20 3688 8
# 15 40 6018 7
# 19 20 7651 6
# 11 40 7587 5
# 10 20 504 5
# 18 40 3312 3
# 20 17 5689 3
# 5 45 6020 2
# 14 40 5408 1
# Explanation
# The data for wands of age 45 (code 1): 

# The minimum number of galleons needed for wand(age = 45, power = 2) = 6020
# The minimum number of galleons needed for wand(age = 45, power = 10) = 1647
# The data for wands of age 40 (code 2): 

# The minimum number of galleons needed for wand(age = 40, power = 1) = 5408
# The minimum number of galleons needed for wand(age = 40, power = 3) = 3312
# The minimum number of galleons needed for wand(age = 40, power = 5) = 7587
# The minimum number of galleons needed for wand(age = 40, power = 7) = 6018
# The data for wands of age 20 (code 4): 


# The minimum number of galleons needed for wand(age = 20, power = 5) = 504
# The minimum number of galleons needed for wand(age = 20, power = 6) = 7651
# The minimum number of galleons needed for wand(age = 20, power = 8) = 3688
# The data for wands of age 17 (code 5): 

# The minimum number of galleons needed for wand(age = 17, power = 3) = 5689
# The minimum number of galleons needed for wand(age = 17, power = 10) = 9897

#-----------------------------------------------------------------------------------

#     Sorun
# Harry Potter ve arkadaşları Ron ile Ollivander's'ta, sonunda Charlie'nin eski kırık asasının yerini alıyor.

# Hermione, seçmenin en iyi yolunun, yüksek güç ve yaştaki şeytani olmayan her bir asayı satın almak için gereken minimum altın kalyon sayısını belirlemek olduğuna karar verir. Ron'un ilgilendiği asaların kimliğini, yaşını, gerekli madeni paraları ve gücünü azalan güç sırasına göre sıralayarak yazdırmak için bir sorgu yazın. Birden fazla değnek aynı güce sahipse, sonucu azalan yaşa göre sıralayın.

# Giriş Formatı
# Aşağıdaki tablolar Ollivander'ın envanterindeki asalarla ilgili verileri içerir:

# Asalar: Kimlik asanın kimliğidir, kod asanın kodudur, coin_needed asayı satın almak için gereken toplam altın kalyon sayısıdır ve güç asanın kalitesini gösterir (güç ne kadar yüksekse o kadar iyidir) değnek).
# Wands_Property: Kod asanın kodudur, age asanın yaşıdır ve is_evil asanın karanlık sanatlar için iyi olup olmadığını gösterir. is_evil değeri 0 ise asanın kötü olmadığı anlamına gelir. Kod ve yaş arasındaki eşleme bire birdir, yani iki çift varsa, (kod1, yaş1) ve (kod2, yaş2), kod1 != kod2 ve yaş1 != yaş2.
# Örnek Giriş

# Asalar Tablosu

# Wands_Özellik Tablosu:

# Örnek Çıktı


# 9 45 1647 10
# 12 17 9897 10
# 1 20 3688 8
# 15 40 6018 7
# 19 20 7651 6
# 11 40 7587 5
# 10 20 504 5
# 18 40 3312 3
# 20 17 5689 3
# 5 45 6020 2
# 14 40 5408 1
# Açıklama
# 45 yaşındaki değnek verileri (kod 1):

# Asa için gereken minimum kalyon sayısı(yaş = 45, güç = 2) = 6020
# Asa için gereken minimum kalyon sayısı(yaş = 45, güç = 10) = 1647
# 40 yaşındaki değnek verileri (kod 2):

# Asa için gereken minimum kalyon sayısı(yaş = 40, güç = 1) = 5408
# Asa için gereken minimum kalyon sayısı(yaş = 40, güç = 3) = 3312
# Asa için gereken minimum kalyon sayısı(yaş = 40, güç = 5) = 7587
# Asa için gereken minimum kalyon sayısı(yaş = 40, güç = 7) = 6018
# 20 yaşındaki değnek verileri (kod 4):


# Asa için gereken minimum kalyon sayısı(yaş = 20, güç = 5) = 504
# Asa için gereken minimum kalyon sayısı(yaş = 20, güç = 6) = 7651
# Asa için gereken minimum kalyon sayısı(yaş = 20, güç = 8) = 3688
# 17 yaşındaki değnek verileri (kod 5):

# Asa için gereken minimum kalyon sayısı(yaş = 17, güç = 3) = 5689
# Asa için gereken minimum kalyon sayısı(yaş = 17, güç = 10) = 9897

SELECT a.id, 
   b.age, 
   a.coins_needed, 
   a.power 
FROM   wands a 
   JOIN wands_property b 
     ON a.code = b.code 
WHERE  b.is_evil = 0 
    AND a.coins_needed = (SELECT Min(a1.coins_needed) 
    FROM   wands a1 
        JOIN wands_property b1 
          ON a1.code = b1.code 
    WHERE  b.age = b1.age 
        AND a.power = a1.power) 
ORDER  BY a.power DESC, 
          b.age DESC;