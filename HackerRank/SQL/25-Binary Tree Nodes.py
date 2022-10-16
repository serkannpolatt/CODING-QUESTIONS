# Problem
# You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

# Column	Type
# N	Integer
# P	Integer
# Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

# Root: If node is root node.
# Leaf: If node is leaf node.
# Inner: If node is neither root nor leaf node.
# Sample Input

# N	P
# 1	2
# 3	2
# 6	8
# 9	8
# 2	5
# 8	5
# 5	null
# Sample Output

# 1 Leaf
# 2 Inner
# 3 Leaf
# 5 Root
# 6 Leaf
# 8 Inner
# 9 Leaf

#------------------------------------------------------------

# Sorun
# Size iki sütun içeren bir BST tablosu verilir: N ve P, burada N, İkili Ağaçtaki bir düğümün değerini temsil eder ve P, N'nin ebeveynidir.

# Sütun Türü
# N Tamsayı
# P Tamsayı
# Düğümün değerine göre sıralanan İkili Ağacın düğüm türünü bulmak için bir sorgu yazın. Her düğüm için aşağıdakilerden birinin çıktısını alın:

# Kök: Düğüm kök düğüm ise.
# Yaprak: Düğüm yaprak düğüm ise.
# İç: Düğüm ne kök ne de yaprak düğüm ise.
# Örnek Giriş

# N P
# 1 2
# 3 2
# 6 8
# 9 8
# 2 5
# 8 5
# 5 boş
# Örnek Çıktı

# 1 Yaprak
# 2 İç
# 3 Yaprak
# 5 Kök
# 6 Yaprak
# 8 İç
# 9 Yaprak

SELECT N, IF(P IS NULL,"Root",IF((SELECT COUNT(*) FROM BST WHERE P=B.N)>0,"Inner","Leaf")) FROM BST AS B ORDER BY N;