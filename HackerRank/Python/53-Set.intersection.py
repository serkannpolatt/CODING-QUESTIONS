# Task
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

# Input Format
# The first line contains n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.

# Constraints
# 0 < Total number of students in college < 1000
# Output Format
# Output the total number of students who have subscriptions to both English and French newspapers.

# Sample Input


# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

# 5
# Explanation

# The roll numbers of students who have both subscriptions:
# 1, 2, 3, 6 and 8.
# Hence, the total is 5 students.

#-------------------------------------------------------------

# Görev
# District College öğrencilerinin İngilizce ve Fransızca gazetelere abonelikleri vardır. Bazı öğrenciler sadece İngilizce'ye abone olmuş, bazıları sadece Fransızca'ya abone olmuş, bazıları ise her iki gazeteye de abone olmuştur.

# Size iki takım öğrenci rulo numarası verilir. Bir takım İngiliz gazetesine, bir takım Fransız gazetesine abone oldu. Göreviniz, her iki gazeteye de abone olan toplam öğrenci sayısını bulmaktır.

# Giriş Formatı
# İlk satırda İngilizce gazeteye abone olan öğrenci sayısı n'dir.
# İkinci satır, bu öğrencilerin n boşlukla ayrılmış rulo numaralarını içerir.
# Üçüncü satır, Fransız gazetesine abone olan öğrenci sayısı olan b'yi içermektedir.
# Dördüncü satır, bu öğrencilerin b boşlukla ayrılmış rulo numaralarını içerir.

# Kısıtlamalar
# 0 < Üniversitedeki toplam öğrenci sayısı < 1000
# Çıkış formatı
# Hem İngilizce hem de Fransızca gazetelere abone olan toplam öğrenci sayısını çıktılayın.

# Örnek Giriş


# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Örnek Çıktı

# 5
# Açıklama

# Her iki aboneliğe de sahip olan öğrencilerin sıra numaraları:
# 1, 2, 3, 6 ve 8.
# Buna göre toplam 5 öğrencidir.

# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

print(len(SET_N & SET_B))