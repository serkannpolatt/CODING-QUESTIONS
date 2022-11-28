# Task
# You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# Note: Each input line ends with a “\n” character.

# Constraints
# 1 <= n <= 105
# The sum of the lengths of all the words do not exceed 106 
# All the words are composed of lowercase English letters only.
# Input Format
# The first line contains the integer, n.
# The next n lines each contain a word.

# Output Format
# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output

# 3
# 2 1 1
# Explanation


# There are 3 distinct words. Here, “bcdef” appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are “bcdef”, “abcdefg” and “bcde” which corresponds to the output.

#-------------------------------------------------------------

# Görev
# Size n kelime verildi. Bazı kelimeler tekrar edebilir. Her kelime için, oluşum sayısını çıktılayın. Çıkış sırası, kelimenin giriş sırasına karşılık gelmelidir. Açıklama için örnek giriş/çıkışa bakın.

# Not: Her giriş satırı bir “\n” karakteri ile biter.

# Kısıtlamalar
# 1 <= n <= 105
# Tüm kelimelerin uzunluklarının toplamı 106'yı geçmez
# Tüm kelimeler sadece küçük İngilizce harflerden oluşmaktadır.
# Giriş Formatı
# İlk satır n tamsayısını içerir.
# Sonraki n satırın her biri bir kelime içerir.

# Çıkış formatı
# Çıktı 2 satır.
# İlk satırda, girdiden farklı kelimelerin sayısını çıktılayın.
# İkinci satırda, girişteki görünümlerine göre her bir farklı kelime için oluşum sayısını çıktılayın.

# Örnek Giriş

# 4
#bcdef
# abcdefg
#bcde
#bcdef
# Örnek Çıktı

# 3
# 2 1 1
# Açıklama


# 3 ayrı kelime vardır. Burada, girişte ilk ve son konumlarda iki kez “bcdef” görünür. Diğer kelimeler birer kez görünür. İlk görünümlerin sırası çıktıya karşılık gelen “bcdef”, “abcdefg” ve “bcde” şeklindedir.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

N = int(input())
LIST = []

for i in range(N):
    LIST.append(input().strip())

COUNT = Counter(LIST)

print(len(COUNT))
print(*COUNT.values())