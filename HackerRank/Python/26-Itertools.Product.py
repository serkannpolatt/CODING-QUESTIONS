# Problem
# This tool computes the cartesian product of input iterables.

# It is equivalent to nested for-loops.

# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

# Task
# You are given a two lists A and B. Your task is to compute their cartesian product AXB.

# Note: A and B are sorted lists, and the cartesian product’s tuples should be output in sorted order.

# Input Format
# The first line contains the space separated elements of list A.

# The second line contains the space separated elements of list B.


# Both lists have no duplicate integer elements.

# Constraints
# 0 < A < B
# 0 < B < 30

# Output Format
# Output the space separated tuples of the cartesian product.

#---------------------------------------------------

# Sorun
# Bu araç, girdi yinelenebilirlerinin kartezyen çarpımını hesaplar.

# Yuvalanmış for döngülerine eşdeğerdir.

# Örneğin, product(A, B), A'daki x için ((x,y) ile B'deki y) ile aynı şeyi döndürür.

# Görev
# Size A ve B olmak üzere iki liste veriliyor. Göreviniz onların kartezyen ürünü AXB'yi hesaplamak.

# Not: A ve B sıralı listelerdir ve kartezyen ürünün demetleri sıralı düzende çıkarılmalıdır.

# Giriş Formatı
# İlk satır, A listesinin boşlukla ayrılmış öğelerini içerir.

# İkinci satır, B listesinin boşlukla ayrılmış öğelerini içerir.


# Her iki listede de yinelenen tamsayı öğesi yok.

# Kısıtlamalar
# 0 < A < B
# 0 < B < 30

# Çıkış formatı
# Kartezyen çarpımının boşlukla ayrılmış demetlerinin çıktısını alın.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product 
a = map(int, input().split())
b = map(int, input().split())
print(*product(a, b))

