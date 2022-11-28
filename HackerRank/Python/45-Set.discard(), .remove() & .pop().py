# Task
# You have a non-empty set s, and you have to execute N commands given in N lines.

# The commands will be pop, remove and discard.

# Input Format
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

# Constraints
# 0 < n <20
# 0 < N < 20
# Output Format
# Print the sum of the elements of set s on a single line.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5
# Sample Output

# 4
# Explanation

# After completing these 10 operations on the set, we get set(|4|). Hence, the sum is 4.

# Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.

#-------------------------------------------------------------

# Görev
# Boş olmayan bir kümeniz var ve N satırda verilen N komutu çalıştırmanız gerekiyor.

# Komutlar açılır, kaldırılır ve atılır.

# Giriş Formatı
# İlk satır, s kümesindeki öğelerin sayısı olan n tamsayısını içerir.
# İkinci satır, küme s'nin n boşlukla ayrılmış öğelerini içerir. Tüm öğeler, 9'dan küçük veya ona eşit, negatif olmayan tam sayılardır.
# Üçüncü satır, komutların sayısı olan N tamsayısını içerir.
# Sonraki N satır ya pop, remove ve/veya discard komutlarını ve ardından ilişkili değerleri içerir.

# Kısıtlamalar
# 0 < n <20
# 0 < N < 20
# Çıkış formatı
# set s öğelerinin toplamını tek bir satıra yazdırın.

# Örnek Giriş

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# 9'u kaldır
# at 9
# at 8
# 7'yi kaldır
# pop
# at 6
# 5'i kaldır
# pop
# at 5
# Örnek Çıktı

# 4
# Açıklama

# Sette bu 10 işlemi tamamladıktan sonra set(|4|) alıyoruz. Dolayısıyla toplam 4'tür.

# Not: Atarken set s öğelerini tam sayılara dönüştürün. Setin doğru girilmesini sağlamak için ilk iki kod satırını editöre ekledik.

n = int(input())
s = set(map(int, input().split())) # Set of n elements

for i in range(int(input())): # Iterate in range of the input num
    s1 = input().split()
    if s1[0] == 'pop':
        s.pop()
    elif s1[0] == 'remove':
        s.remove(int(s1[1]))
    elif s1[0] == 'discard':
        s.discard(int(s1[1]))

print(sum(s))