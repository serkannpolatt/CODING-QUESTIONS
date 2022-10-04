# Task
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i2 . 

# Input Format
# The first and the only line contains the integer, n.

# Constraints
# 1 ≤ n ≤ 20

# Output Format
# Print n lines, one corresponding to each i.

#---------------------------------------------------

# Görev
# Sağlanan kod saplaması okur ve STDIN'den tamsayı, n. Tüm negatif olmayan tamsayılar için i < n, i2 yazdırın.

# Giriş Formatı
# İlk ve tek satır n tamsayısını içerir.

# Kısıtlamalar
# 1 ≤ n ≤ 20

# Çıkış formatı
# Her bir i'ye karşılık gelen n satır yazdırın.

if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i ** 2)