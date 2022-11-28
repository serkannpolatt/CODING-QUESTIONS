# Task
# Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Constraints
# 0 < Total number of students in colleges < 1000
# Output Format
# Output the total number of students who are subscribed to the English newspaper only.

# Sample Input


# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

# 4
# Explanation

# The roll numbers of students who only have English newspaper subscriptions are:
# 4, 5, 7 and 9.
# Hence, the total is 4 students.

#-------------------------------------------------------------

# Görev
# District College öğrencilerinin İngilizce ve Fransızca gazetelere aboneliği vardır. Bazı öğrenciler sadece İngilizce gazeteye abone olmuş, bazıları sadece Fransız gazetesine abone olmuş, bazıları ise her iki gazeteye de abone olmuştur.

# Size iki takım öğrenci rulo numarası verilir. Bir takım İngiliz gazetesine, bir takım Fransız gazetesine abone oldu. Göreviniz, yalnızca İngilizce gazetelere abone olan toplam öğrenci sayısını bulmaktır.

# Giriş Formatı
# İlk satırda İngilizce gazetesine abone olan öğrenci sayısı yer almaktadır.
# İkinci satır, İngilizce gazetesine abone olan öğrenci rulo numaralarının boşlukla ayrılmış listesini içerir.
# Üçüncü satır, Fransız gazetesine abone olan öğrenci sayısını içerir.
# Dördüncü satır, Fransız gazetesine abone olan öğrenci rulo numaralarının boşlukla ayrılmış listesini içerir.

# Kısıtlamalar
# 0 < Kolejlerdeki toplam öğrenci sayısı < 1000
# Çıkış formatı
# Yalnızca İngilizce gazetesine abone olan toplam öğrenci sayısını çıktılayın.

# Örnek Giriş


# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Örnek Çıktı

# 4
# Açıklama

# Yalnızca İngilizce gazete aboneliği olan öğrencilerin sıra numaraları:
# 4, 5, 7 ve 9.
# Buna göre toplam 4 öğrencidir.

# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

NEW_SET = SET_N.difference(SET_B)
print(len(NEW_SET))