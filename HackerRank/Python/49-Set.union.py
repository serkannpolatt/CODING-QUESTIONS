# Task
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

# Input Format
# The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b, the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.

# Constraints
# 0 < Total number of students in college < 1000
# Output Format
# Output the total number of students who have at least one subscription.


# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

# 13
# Explanation


# Roll numbers of students who have at least one subscription:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21 and 55. Roll numbers: 1 ,2, 3, 6 and 8 are in both sets so they are only counted once.
# Hence, the total is 13 students.

#-------------------------------------------------------------

# Görev
# District College öğrencilerinin İngilizce ve Fransızca gazetelere abonelikleri vardır. Bazı öğrenciler sadece İngilizce'ye abone olmuş, bazıları sadece Fransızca'ya abone olmuş, bazıları ise her iki gazeteye de abone olmuştur.

# Size iki takım öğrenci rulo numarası verilir. Bir takım İngiliz gazetesine, diğer takım Fransız gazetesine abone oldu. Aynı öğrenci her iki kümede de olabilir. Göreviniz, en az bir gazeteye abone olan toplam öğrenci sayısını bulmaktır.

# Giriş Formatı
# İlk satır, İngilizce gazetesine abone olan öğrenci sayısı olan n tamsayısını içerir.
# İkinci satır, bu öğrencilerin n boşlukla ayrılmış rulo numaralarını içerir.
# Üçüncü satır, Fransız gazetesine abone olan öğrenci sayısı olan b'yi içermektedir.
# Dördüncü satır, bu öğrencilerin b boşlukla ayrılmış rulo numaralarını içerir.

# Kısıtlamalar
# 0 < Üniversitedeki toplam öğrenci sayısı < 1000
# Çıkış formatı
# En az bir aboneliği olan toplam öğrenci sayısını çıktılayın.


# Örnek Giriş

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Örnek Çıktı

# 13
# Açıklama


# En az bir aboneliği olan öğrencilerin rulo sayıları:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21 ve 55. Rulo numaraları: 1 ,2, 3, 6 ve 8 her iki sette olduğundan sadece bir kez sayılırlar.
# Buna göre toplam 13 öğrencidir.


# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

NEW_SET = SET_N.union(SET_B)
print(len(NEW_SET))