# Task
# Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Constraints
# 0 < Total number of students in college < 1000
# Output Format
# Output total number of students who have subscriptions to the English or the French newspaper but not both.

# Sample Input


# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

# 8
# Explanation

# The roll numbers of students who have subscriptions to English or French newspapers but not both are:
# 4, 5, 7, 9, 10, 11, 21 and 55.
# Hence, the total is 8 students.

#-------------------------------------------------------------

# Görev
# District College öğrencilerinin İngilizce ve Fransızca gazetelere abonelikleri vardır. Bazı öğrenciler yalnızca İngilizce'ye abone olmuş, bazıları yalnızca Fransızca'ya abone olmuş, bazıları ise her iki gazeteye de abone olmuştur.

# Size iki takım öğrenci rulo numarası verilir. Bir takım İngiliz gazetesine, bir takım Fransız gazetesine abone oldu. Göreviniz, İngiliz veya Fransız gazetesine abone olan ancak her ikisine birden abone olmayan toplam öğrenci sayısını bulmaktır.

# Giriş Formatı
# İlk satırda İngilizce gazetesine abone olan öğrenci sayısı yer almaktadır.
# İkinci satır, İngilizce gazetesine abone olan öğrenci rulo numaralarının boşlukla ayrılmış listesini içerir.
# Üçüncü satır, Fransız gazetesine abone olan öğrenci sayısını içerir.
# Dördüncü satır, Fransız gazetesine abone olan öğrenci rulo numaralarının boşlukla ayrılmış listesini içerir.

# Kısıtlamalar
# 0 < Üniversitedeki toplam öğrenci sayısı < 1000
# Çıkış formatı
# Çıktı İngiliz veya Fransız gazetesine abone olan ancak her ikisine birden abone olmayan öğrencilerin toplam sayısı.

# Örnek Giriş


# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Örnek Çıktı

# 8
# Açıklama

# İngilizce veya Fransızca gazetelere aboneliği olan ancak her ikisine birden abone olmayan öğrencilerin rulo sayıları:
# 4, 5, 7, 9, 10, 11, 21 ve 55.
# Buna göre toplam 8 öğrencidir.

# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

print(len(SET_N.symmetric_difference(SET_B)))