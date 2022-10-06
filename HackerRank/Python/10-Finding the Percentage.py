# Task
# The provided code stub read in a dictionary containing key/value pairs of name:[Marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example

# marks key: value pairs are
# ‘alpha’:[20, 30, 40]
# ‘beta’:[30, 50, 70]
# query_name = ‘beta’

# The query_name is ‘beta’. beta’s average score is (30 + 50 + 70)/3 = 50.0.

# Input Format
# The first line contains the integer n, the number of students’s records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name , the name of a student to query.

# Constraints
# 2 ≤ n ≤ 10
# 0 ≤ marks[i] ≤ 100
# length of the marks array = 3
# Output Format
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

#---------------------------------------------------

# Görev
# Sağlanan kod saplaması, bir öğrenci listesi için anahtar/değer çiftlerini içeren bir sözlükte okunur:[İşaretler]. Sağlanan öğrenci adı için işaretler dizisinin ortalamasını ondalıktan sonra 2 basamak göstererek yazdırın.

# Örnek

# işaret anahtarı: değer çiftleri
# "alfa":[20, 30, 40]
# "beta":[30, 50, 70]
# sorgu_adı = "beta"

# Sorgu_adı "beta"dır. beta'nın ortalama puanı (30 + 50 + 70)/3 = 50.0'dır.

# Giriş Formatı
# İlk satır, öğrenci kayıtlarının sayısı olan n tamsayısını içerir. Sonraki n satır, bir öğrenci tarafından elde edilen adları ve işaretleri içerir, her değer bir boşlukla ayrılır. Son satır, sorgulanacak bir öğrencinin adı olan sorgu_adı içerir.

# Kısıtlamalar
# 2 ≤ n ≤ 10
# 0 ≤ işaret[i] ≤ 100
# işaret dizisinin uzunluğu = 3
# Çıkış formatı
# Bir satır yazdır: Belirli bir öğrenci tarafından elde edilen notların ortalaması 2 ondalık basamağa göre düzeltilir.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])    
per = sum(output)/len(output);
print("%.2f" % per);    