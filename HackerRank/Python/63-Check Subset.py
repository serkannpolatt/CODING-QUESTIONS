# Task
# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Input Format
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of set B.

# Constraints
# 0 < T < 21
# 0 < Number of elements in each set < 1001
# Output Format
# Output True or False for each test case on separate lines.

# Sample Input

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
# Sample Output

# True 
# False
# False
# Explanation


# Test Case 01 Explanation

# Set A = {1 2 3 5 6}
# Set B = {9 8 5 6 3 2 1 4 7}
# All the elements of set A are elements of set B.
# Hence, set A is a subset of set B.

#------------------------------------------------------------

# Görev
# Size A ve B olmak üzere iki set verilir.
# İşiniz A kümesinin B kümesinin bir alt kümesi olup olmadığını bulmak.

# A kümesi, B kümesinin alt kümesiyse, True yazdırın.
# A kümesi, B kümesinin bir alt kümesi değilse, Yanlış yazdırın.

# Giriş Formatı
# İlk satır, test senaryolarının sayısını içerecektir, T.
# Her test durumunun ilk satırı, A kümesindeki öğelerin sayısını içerir.
# Her test durumunun ikinci satırı, A kümesinin boşlukla ayrılmış öğelerini içerir.
# Her test durumunun üçüncü satırı, B kümesindeki öğelerin sayısını içerir.
# Her test durumunun dördüncü satırı, B kümesinin boşlukla ayrılmış öğelerini içerir.

# Kısıtlamalar
# 0 < T < 21
# 0 < Her kümedeki eleman sayısı < 1001
# Çıkış formatı
# Ayrı satırlarda her test durumu için Doğru veya Yanlış çıktısı alın.

# Örnek Giriş

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
# Örnek Çıktı

# Doğru
# Yanlış
# Yanlış
# Açıklama


# Test Durumu 01 Açıklama

# A kümesi = {1 2 3 5 6}
# B'yi ayarla = {9 8 5 6 3 2 1 4 7}
# A kümesinin tüm elemanları B kümesinin elemanlarıdır.
# Dolayısıyla A kümesi, B kümesinin bir alt kümesidir.

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a = int(input())
    set_a = set(map(int, input().split()))

    b = int(input())
    set_b = set(map(int, input().split()))

    if len(set_a - set_b) == 0:
        print("True")
    else:
        print("False")