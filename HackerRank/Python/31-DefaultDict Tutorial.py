#  Task
# The defaultdict tool is a container in the collections class of Python. It’s similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn’t use a defaultdict you’d have to check to see if that key exists, and if it doesn’t, set it to what you want.

# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

# Example

# Group A contains ‘a’, ‘b’, ‘a’ Group B contains ‘a’, ‘c’

# For the first word in group B, ‘a’, it appears at positions 1 and 3 in group A. The second word, ‘c’, does not appear in group A, so print -1.

# Input Format
# The first line contains integers, n and m separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.

# Constraints
# 1 <= n <= 10000
# 1 <= m <= 100
# 1 <= length of each word in the input <= 100
# Output Format
# Output m lines.
# The ith line should contain the 1-indexed positions of the occurrences of the ith word separated by spaces.

# Explanation

# ‘a’ appeared 3 times in positions 1, 2 and 4.
# ‘b’ appeared 2 times in positions 3 and 5.
# In the sample problem, if ‘c’ also appeared in word group B, you would print -1.

#---------------------------------------------------

# Görev
# defaultdict aracı, Python'un collections sınıfındaki bir kapsayıcıdır. Her zamanki sözlük (dict) kabına benzer, ancak tek fark, o anahtar henüz ayarlanmamışsa bir defaultdict'in varsayılan bir değere sahip olmasıdır. Bir defaultdict kullanmadıysanız, o anahtarın var olup olmadığını kontrol etmeniz ve yoksa, istediğiniz gibi ayarlamanız gerekir.

# Bu yarışmada size 2 tam sayı verilecektir, n ve m. A kelime grubunda tekrar edebilecek n adet kelime bulunmaktadır. B kelime grubuna ait m adet kelime bulunmaktadır. Her m kelime için kelimenin A grubunda olup olmadığını kontrol ediniz. A grubundaki her m oluşumunun indekslerini yazdırın. Görünmüyorsa, -1 yazdırın.

# Örnek

# A Grubu 'a', 'b', 'a' içerir B Grubu 'a', 'c' içerir

# B grubundaki ilk kelime olan 'a' için, A grubunda 1 ve 3 numaralı konumlarda görünür. İkinci kelime olan 'c', A grubunda görünmez, bu nedenle -1 yazdırın.

# Giriş Formatı
# İlk satır, boşlukla ayrılmış n ve m tamsayılarını içerir.
# Sonraki n satır, A grubuna ait kelimeleri içerir.
# Sonraki m satırı B grubuna ait kelimeleri içerir.

# Kısıtlamalar
# 1 <= n <= 10000
# 1 <= m <= 100
# 1 <= girişteki her kelimenin uzunluğu <= 100
# Çıkış formatı
# Çıktı m satırları.
# i. satır, boşluklarla ayrılmış i. kelimenin oluşumlarının 1-dizinli konumlarını içermelidir.

# Açıklama

# 'a' 1, 2 ve 4 numaralı pozisyonlarda 3 kez göründü.
# 'b' 3 ve 5 pozisyonlarında 2 kez göründü.
# Örnek problemde, B kelime grubunda 'c' de görünüyorsa, -1 yazdırırsınız.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    d[input()].append(str(i + 1))
for j in range(m):
    print(' '.join(d[input()]) or -1)