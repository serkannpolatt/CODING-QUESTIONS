# Task
# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools .

# You are given a string S. Suppose a character ‘c‘ occurs consecutively X times in the string. Replace these consecutive occurrences of the character ‘c‘ with (X, c) in the string.

# Input Format
# A single line of input consisting of the string S.

# Output Format
# A single line of output consisting of the modified string.

# Constraints
# All the characters of S denote integers between 0 and 9.
# 1 <= |S| <= 104
# Sample Input

# 1222311
# Sample Output

# (1, 1) (3, 2) (1, 3) (2, 1)
# Explanation


# First, the character 1 occurs only once. It is replaced by (1 , 1). Then the character 2 occurs three times, and it is replaced by (3, 2) and so on.

# Also, note the single space within each compression and between the compressions.

#-------------------------------------------------------------

# Görev
# Bu görevde, itertools'un groupby() işlevinin kullanışlılığını takdir etmenizi istiyoruz.

# Size bir S dizisi verildi. Diyelim ki bir 'c' karakteri dizide art arda X kez geçiyor. 'c' karakterinin bu ardışık oluşumlarını dizedeki (X, c) ile değiştirin.

# Giriş Formatı
# S dizesinden oluşan tek bir girdi satırı.

# Çıkış formatı
# Değiştirilen dizeden oluşan tek bir çıktı satırı.

# Kısıtlamalar
# S'nin tüm karakterleri 0 ile 9 arasındaki tam sayıları ifade eder.
# 1 <= |S| <= 104
# Örnek Giriş

# 1222311
# Örnek Çıktı

# (1, 1) (3, 2) (1, 3) (2, 1)
# Açıklama


# İlk olarak, 1 karakteri yalnızca bir kez geçer. (1 , 1) ile değiştirilir. Daha sonra 2 karakteri üç kez oluşur ve yerine (3, 2) vb. gelir.

# Ayrıca, her sıkıştırma içindeki ve sıkıştırmalar arasındaki tek boşluğa dikkat edin.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

for k, c in groupby(input()):
    print("(%d, %d)" % (len(list(c)), int(k)), end=' ')