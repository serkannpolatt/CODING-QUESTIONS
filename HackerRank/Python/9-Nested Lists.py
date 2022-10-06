# Problem
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# records  = [[ “chi”, 20.0]], [“beta”, 50.0], [“alpha”, 50.0]

# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: [“beta”, “alpha”]. Ordered alphabetically, the names are printed as:

# Input Format
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.

# The first line contains a student’s name.
# The second line contains their grade.
# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.
# Output Format
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

#---------------------------------------------------

# Sorun
# N öğrencilik bir sınıftaki her öğrencinin adı ve notları verildiğinde, bunları iç içe bir listede saklayın ve ikinci en düşük nota sahip herhangi bir öğrencinin adını/adlarını yazdırın.

# Not: İkinci en düşük sınıfa sahip birden fazla öğrenci varsa, adlarını alfabetik olarak sıralayın ve her adı yeni bir satıra yazdırın.

# Örnek

# kayıt = [[ “chi”, 20.0]], [“beta”, 50.0], [“alfa”, 50.0]

# Sıralı puan listesi [20.0, 50.0]'dır, bu nedenle ikinci en düşük puan 50.0'dır. Bu puana sahip iki öğrenci var: [“beta”, “alfa”]. Alfabetik olarak sıralandığında, isimler şu şekilde yazdırılır:

# Giriş Formatı
# İlk satır, öğrenci sayısını içeren bir tamsayı içerir.
# Sonraki satırlar, her öğrenciyi satırlar üzerinden tanımlar.

# İlk satır bir öğrencinin adını içerir.
# İkinci satır onların derecesini içerir.
# Kısıtlamalar
# 2 <= N <= 5
# Her zaman ikinci en düşük notu alan bir veya daha fazla öğrenci olacaktır.
# Çıkış formatı
# İkinci en düşük nota sahip öğrenci(ler)in isim(ler)ini yazdırın. Birden fazla öğrenci varsa, isimlerini alfabetik olarak sıralayın ve her birini yeni bir satıra yazdırın.

Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    b=sorted(list(set(scorelist)))[1] 
    for a,c in sorted(Result):
        if c==b:
            print(a)