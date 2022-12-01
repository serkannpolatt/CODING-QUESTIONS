# Task
# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.

# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# Example
# Set ([1 , 3, 4]) is a strict superset of set ([1 , 3]).
# Set ([1 , 3, 4]) is not a strict superset of set ([1 , 3, 4]).
# Set ([1 , 3, 4]) is not a strict superset of set ([1 , 3, 5]).

# Input Format
# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the space separated elements of the other sets.

# Constraints
# 0 < len(set(A)) < 501
# 0 < N < 21
# 0 < len(otherSets) < 101
# Output Format
# Print True if set A is a strict superset of all other N sets. Otherwise, print False.

# Sample Input 0


# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Sample Output 0

# False
# Explanation 0

# Set A is the strict superset of the set ([1, 2, 3, 4, 5]) but not of the set ([100, 11, 12]) because 100 is not in set A.
# Hence, the output is False.


#------------------------------------------------------------

# Görev
# Size bir A kümesi ve n tane başka küme verilir.
# İşiniz, A kümesinin N kümelerinin her birinin katı bir üst kümesi olup olmadığını bulmaktır.

# A, N kümelerinin her birinin katı bir üst kümesiyse, Doğru Yazdır. Aksi takdirde, Yanlış yazdırın.

# Kesin bir üst küme, alt kümesinde bulunmayan en az bir öğeye sahiptir.

# Örnek
# Küme ([1 , 3, 4]), kümenin katı bir üst kümesidir ([1 , 3]).
# Küme ([1 , 3, 4]), kümenin katı bir üst kümesi değildir ([1 , 3, 4]).
# Küme ([1 , 3, 4]), kümenin katı bir üst kümesi değildir ([1 , 3, 5]).

# Giriş Formatı
# İlk satır, A kümesinin boşlukla ayrılmış öğelerini içerir.
# İkinci satır, diğer kümelerin sayısı olan n tamsayısını içerir.
# Sonraki n satır, diğer kümelerin boşlukla ayrılmış öğelerini içerir.

# Kısıtlamalar
# 0 < len(set(A)) < 501
# 0 < N < 21
# 0 < len(diğer Kümeler) < 101
# Çıkış formatı
# A kümesi diğer tüm N kümelerinin katı bir üst kümesiyse Doğru Yazdır. Aksi takdirde, Yanlış yazdırın.

# Örnek Giriş 0


# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12
# Örnek Çıktı 0

# Yanlış
# Açıklama 0

# A kümesi ([1, 2, 3, 4, 5]) kümesinin katı üst kümesidir, ancak ([100, 11, 12]) kümesinin değildir çünkü 100, A kümesinde değildir.
# Dolayısıyla çıktı False'dır.


# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
COUNT = 0
VALUE = 0

for i in range(int(input())):
    if A.issuperset(set(input().split())):
        COUNT += 1
    else:
        VALUE += 1
if VALUE != 0:
    print('False')
else:
    print('True')