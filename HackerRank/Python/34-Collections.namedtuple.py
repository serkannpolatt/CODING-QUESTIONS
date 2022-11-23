# Objective
# Collections.namedtuple()
# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

# Task
# Dr. John Wesley has a spreadsheet containing a list of student’s IDs, marks, class and name.

# Your task is to help Dr. Wesley calculate the average marks of the students.

# Average = Sum of all marks / Total Students

# Note:
# 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
# 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won’t change.)


# Input Format
# The first line contains an integer N, the total number of students.
# The second line contains the names of the columns in any order.
# The next N lines contains the marks, IDs, name and class, under their respective column names.

# Constraints
# 0 < N <= 100
# Output Format
# Print the average marks of the list corrected to 2 decimal places.

#-------------------------------------------------------------

# Amaç
# Collections.namedtuple()
# Temel olarak, adlandırılmış kümeler oluşturması kolay, hafif nesne türleridir.
# Tuple'ları basit görevler için uygun kaplara dönüştürürler.
# Nametuples ile, bir grubun üyelerine erişmek için tamsayı indeksleri kullanmak zorunda değilsiniz.

# Görev
# Dr. John Wesley'nin öğrenci kimliklerinin, notlarının, sınıfının ve adının bir listesini içeren bir elektronik tablosu vardır.

# Göreviniz Dr. Wesley'nin öğrencilerin ortalama notlarını hesaplamasına yardımcı olmaktır.

# Ortalama = Tüm notların toplamı / Toplam Öğrenci

# Not:
# 1. Sütunlar herhangi bir sırada olabilir. Kimlikler, işaretler, sınıf ve ad, elektronik tabloda herhangi bir sırada yazılabilir.
# 2. Sütun adları ID, MARKS, CLASS ve NAME şeklindedir. (Bu adların yazım ve büyük/küçük harf türü değişmeyecektir.)


# Giriş Formatı
# İlk satır, toplam öğrenci sayısı olan bir N tamsayısını içerir.
# İkinci satır, herhangi bir sırayla sütunların adlarını içerir.
# Sonraki N satır, ilgili sütun adlarının altında işaretleri, kimlikleri, adı ve sınıfı içerir.

# Kısıtlamalar
# 0 < N <= 100
# Çıkış formatı
# 2 ondalık basamağa göre düzeltilmiş listenin ortalama işaretlerini yazdırın.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
fields = input().split()

total_marks = 0
for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))