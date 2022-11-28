# Task
# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format
# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.


# Constraints
# 0 < N <= 100
# Output Format
# Print the space separated elements of deque d.

# Sample Input

# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft
# Sample Output


# 1 2

#-------------------------------------------------------------

# Görev
# Boş bir deque üzerinde append, pop, popleft ve appendleft yöntemlerini gerçekleştirin. d.

# Giriş Formatı
# İlk satır, işlem sayısı olan bir N tamsayısını içerir.
# Sonraki N satır, yöntemlerin boşlukla ayrılmış adlarını ve değerlerini içerir.


# Kısıtlamalar
# 0 < N <= 100
# Çıkış formatı
# deque d'nin boşlukla ayrılmış öğelerini yazdırın.

# Örnek Giriş

# 6
# ekle 1
# ekle 2
# ekle 3
# ek 4
# pop
# popleft
# Örnek Çıktı


# 1 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

D = deque()

for _ in range(int(input())):
    oper, val, *args = input().split() + ['']
    eval(f'D.{oper} ({val})')
print(*D)