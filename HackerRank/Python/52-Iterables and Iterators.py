# Task
# The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

# You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

# Find the probability that at least one of the K indices selected will contain the letter: ‘a‘.

# Input Format
# The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists of N space-separated lowercase English letters, denoting the elements of the list.

# The third and the last line of input contains the integer K, denoting the number of indices to be selected.

# Output Format
# Output a single line consisting of the probability that at least one of the K indices selected contains the letter:’a‘.

# Note: The answer must be correct up to 3 decimal places.


# Constraints
# 1 <= N <= 10
# 1 <= K <= N
# All the letters in the list are lowercase English letters.
# Sample Input

# 4 
# a a c d
# 2
# Sample Output

# 0.8333
# Explanation


# All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
# (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)

# Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter ‘a‘.

# Hence, the answer is 5/6.

#-------------------------------------------------------------

# Görev
# itertools modülü, kendi başlarına veya kombinasyon halinde yararlı olan hızlı, bellek açısından verimli araçlardan oluşan bir çekirdek setini standartlaştırır. Birlikte, saf Python'da özel araçları kısa ve verimli bir şekilde oluşturmayı mümkün kılan bir yineleyici cebir oluştururlar.

# Size N küçük harfli İngilizce harflerden oluşan bir liste verilir. Belirli bir K tamsayısı için, listeden tek tip olasılığa sahip herhangi bir K indeksini (1 tabanlı indeksleme varsayın) seçebilirsiniz.

# Seçilen K indekslerinden en az birinin 'a' harfini içerme olasılığını bulun.

# Giriş Formatı
# Giriş üç satırdan oluşur. İlk satır, listenin uzunluğunu belirten N tamsayısını içerir. Sonraki satır, listenin öğelerini gösteren N boşlukla ayrılmış küçük İngilizce harflerden oluşur.

# Girdinin üçüncü ve son satırı, seçilecek indeks sayısını gösteren K tamsayısını içerir.

# Çıkış formatı
# Seçilen K endekslerinden en az birinin 'a' harfini içerme olasılığından oluşan tek bir satır çıktısı alın.

# Not: Cevap 3 ondalık basamağa kadar doğru olmalıdır.


# Kısıtlamalar
# 1 <= N <= 10
# 1 <= K <= N
# Listedeki tüm harfler küçük İngilizce harflerdir.
# Örnek Giriş

# 4
# bir c d
# 2
# Örnek Çıktı

# 0.8333
# Açıklama


# 1'den 4'e kadar olan indekslerden oluşan 2 uzunluğundaki tüm olası sırasız demetler şunlardır:
# (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)

# Bu 6 kombinasyondan 5'i 'a' harfini içeren indeksler olan indeks 1 veya indeks 2'yi içerir.

# Dolayısıyla cevap 5/6'dır.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
LETTERS = list(input().split(" "))
K = int(input())

TUPLES = list(combinations(LETTERS, K))
CONTAINS = [word for word in TUPLES if "a" in word]

print(len(CONTAINS)/len(TUPLES))