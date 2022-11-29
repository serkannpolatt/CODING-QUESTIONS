# Task
# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

# Your task is to execute those operations and print the sum of elements from set A.

# Input Format
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2 * N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

# 0 < len(set(A)) < 1000 
# 0 < len(otherSets) < 100
# 0 < N < 100

# Output Format
# Output the sum of elements in set A.

# Sample Input

#  16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66
# Sample Output

# 38
# Explanation

# After the first operation, (intersection_update operation), we get:
# set A = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# After the second operation, (update operation), we get:
# set A = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 55, 56]) 

# After the third operation, (symmetric_difference_update operation), we get:
# set A = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 35, 55, 58, 62, 66])

# After the fourth operation, ( difference_update operation), we get:
# set A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# The sum of elements in set A after these operations is 38.

#-------------------------------------------------------------

# Görev
# Size bir set A ve N sayıda başka set verilir. Bu N sayıdaki kümenin, A kümesinde bazı özel mutasyon işlemleri gerçekleştirmesi gerekir.

# Göreviniz bu işlemleri yürütmek ve A kümesindeki öğelerin toplamını yazdırmak.

# Giriş Formatı
# İlk satır, A kümesindeki öğelerin sayısını içerir.
# İkinci satır, A kümesindeki boşlukla ayrılmış öğelerin listesini içerir.
# Üçüncü satır, diğer kümelerin sayısı olan N tamsayısını içerir.
# Sonraki 2 * N satır, her biri iki satır içeren N parçaya bölünmüştür.
# Her bölümün ilk satırı, işlem adının boşlukla ayrılmış girişlerini ve diğer kümenin uzunluğunu içerir.
# Her parçanın ikinci satırı, diğer kümedeki boşlukla ayrılmış öğelerin listesini içerir.

# 0 < len(set(A)) < 1000
# 0 < len(diğer Kümeler) < 100
# 0 < N < 100

# Çıkış formatı
# A kümesindeki elemanların toplamını çıkar.

# Örnek Giriş

# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# kesişme_güncelleme 10
# 2 3 5 6 8 9 1 4 7 11
# güncelleme 2
# 55 66
# simetrik_difference_update 5
# 22 7 35 62 58
# fark_güncelleme 7
# 11 22 35 55 58 62 66
# Örnek Çıktı

# 38
# Açıklama

# İlk işlemden sonra (intersection_update işlemi) şunu elde ederiz:
# küme A = küme([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# İkinci işlemden sonra (güncelleme işlemi) şunu elde ederiz:
# küme A = küme([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 55, 56])

# Üçüncü işlemden (simetrik_fark_güncelleme işlemi) sonra şunu elde ederiz:
# küme A = küme([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 35, 55, 58, 62, 66)

# Dördüncü işlemden sonra ( fark_güncelleme işlemi) şunu elde ederiz:
# küme A = küme([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Bu işlemlerden sonra A kümesindeki elemanların toplamı 38'dir.

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
SET_A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation = input().split()
    new_set = set(map(int, input().split()))
    eval('SET_A.{}({})'.format(operation[0], new_set))

print(sum(SET_A))