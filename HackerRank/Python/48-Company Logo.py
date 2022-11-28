# Task
# A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.
# For example, according to the conditions described above,

# GOOGLE would have it’s logo with the letters G, O, E.

# Input Format
# A single line of input containing the string S.

# Constraints
# 3 < len(S) <104
# S has at least 3 distinct characters
# Output Format
# Print the three most common characters along with their occurrence count each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

# Sample Input 0

# aabbbccde
# Sample Output 0


# b 3
# a 2
# c 2
# Explanation 0

# aabbbccde

# Here, b occurs 3 times. It is printed first.
# Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.


# Note: The string S has at least 3 distinct characters.

#-------------------------------------------------------------

# Görev
# Yeni açılan çok uluslu bir marka, şirket logosunu şirket adındaki en yaygın üç karaktere dayandırmaya karar verdi. Şimdi bu duruma dayalı olarak çeşitli şirket isimleri ve logo kombinasyonlarını deniyorlar. Küçük harflerle şirket adı olan bir dize verildiğinde, göreviniz dizedeki en yaygın üç karakteri bulmaktır.

# En yaygın üç karakteri, oluşum sayılarıyla birlikte yazdırın.
# Azalan oluşum sayısına göre sıralayın.
# Oluşum sayısı aynıysa karakterleri alfabetik sıraya göre sıralayın.
# Örneğin, yukarıda açıklanan koşullara göre,

# GOOGLE logosuna G, O, E harfleriyle sahip olurdu.

# Giriş Formatı
# S dizesini içeren tek bir girdi satırı.

# Kısıtlamalar
# 3 < len(S) <104
# S en az 3 farklı karaktere sahip
# Çıkış formatı
# En yaygın üç karakteri, oluşum sayılarıyla birlikte ayrı bir satırda yazdırın.
# Çıktıyı azalan oluşum sayısına göre sıralayın.
# Oluşum sayısı aynıysa karakterleri alfabetik sıraya göre sıralayın.

# Örnek Giriş 0

# aabbbccde
# Örnek Çıktı 0


# b3
# 2
#c2
# Açıklama 0

# aabbbccde

# Burada b 3 defa oluşur. Önce yazdırılır.
# Hem a hem de c 2 kez oluşur. Alfabede a c'den önce geldiği için ikinci satırda a ve üçüncü satırda c yazdırılır.


# Not: S dizesinin en az 3 farklı karakteri vardır.

from collections import Counter

S = input()
S = sorted(S)

FREQUENCY = Counter(list(S))

for k, v in FREQUENCY.most_common(3):
    print(k, v)