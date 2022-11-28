# Task
# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

# Find the total number of distinct country stamps.

# Input Format
# The first line contains an integer N, the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from.

# Constraints
# 0 < N < 1000
# Output Format
# Output the total number of distinct country stamps on a single line.


# Sample Input

# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
# Sample Output

# 5
# Explanation


# UK and France repeat twice. Hence, the total number of distinct country stamps is 5 (five).

#-------------------------------------------------------------

# Görev
# Arkadaşınız Rupal'a yardım etmek için .add() işlemiyle ilgili bilginizi uygulayın.

# Rupal'ın çok büyük bir ülke pulu koleksiyonu var. Koleksiyonundaki farklı ülke pullarının toplam sayısını saymaya karar verdi. Senden yardım istedi. Pulları N tane ülke pulu yığınından birer birer seçiyorsunuz.

# Farklı ülke damgalarının toplam sayısını bulun.

# Giriş Formatı
# İlk satır, ülke damgalarının toplam sayısı olan bir N tamsayısını içerir.
# Sonraki N satır, damganın geldiği ülkenin adını içerir.

# Kısıtlamalar
# 0 < N < 1000
# Çıkış formatı
# Farklı ülke damgalarının toplam sayısını tek bir satıra yazdırın.


# Örnek Giriş

# 7
# İngiltere
# Çin
# AMERİKA BİRLEŞİK DEVLETLERİ
# Fransa
# Yeni Zelanda
# İngiltere
# Fransa
# Örnek Çıktı

# 5
# Açıklama


# İngiltere ve Fransa iki kez tekrar ediyor. Bu nedenle, farklı ülke pullarının toplam sayısı 5'tir (beş).

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
NAMES = set([])
for i in range(n):
    NAMES.add(input())
print(len(NAMES))