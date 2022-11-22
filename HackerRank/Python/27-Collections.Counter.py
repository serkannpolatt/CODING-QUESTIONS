# Objective
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

# Task
# Raghu is a shoe shop owner. His shop has X number of shoes.

# He has a list containing the size of each shoe he has in his shop.

# There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.

# Input Format
# The first line contains X, the number of shoes.


# The second line contains the space separated list of all the shoe sizes in the shop.

# The third line contains N, the number of customers.

# The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe. 


# Constraints
# 0 < X < 10^3
# 0 < N <= 10^3
# 20 < xi < 100
# 2 < shoe size < 20

# Output Format
# Print the amount of money earned by Raghu.

# Explanation 

# Customer 1: Purchased size 6 shoe for $55.

# Customer 2: Purchased size 6 shoe for $45.

# Customer 3: Size 6 no longer available, so no purchase.


# Customer 4: Purchased size 4 shoe for $40.

# Customer 5: Purchased size 18 shoe for $60.

# Customer 6: Size 10 not available, so no purchase.

# Total money earned = 55 + 45 + 40 + 60 = $200

#--------------------------------------------------------------

# Amaç
# Sayaç, öğeleri sözlük anahtarları olarak depolayan bir kapsayıcıdır ve bunların sayıları, sözlük değerleri olarak depolanır.

# Görev
# Raghu bir ayakkabı dükkanı sahibidir. Dükkanında X sayıda ayakkabı var.

# Dükkânındaki her ayakkabının numarasını içeren bir listesi var.

# İstediği numara ayakkabıyı alırsa xi tutarda para ödemeye razı olan N sayıda müşteri vardır.

# Senin görevin Raghu'nun ne kadar para kazandığını hesaplamak.

# Giriş Formatı
# İlk satırda ayakkabı sayısı olan X bulunur.


# İkinci satır, mağazadaki tüm ayakkabı bedenlerinin boşlukla ayrılmış listesini içerir.

# Üçüncü satır, müşteri sayısı olan N'yi içerir.

# Sonraki N satır, müşteri tarafından istenen ayakkabı bedeninin boşlukla ayrılmış değerlerini ve ayakkabının fiyatı olan xi'yi içerir.


# Kısıtlamalar
# 0 < X ​​< 10^3
# 0 < N <= 10^3
# 20 < xi < 100
# 2 < ayakkabı numarası < 20

# Çıkış formatı
# Raghu tarafından kazanılan para miktarını yazdırın.

# Açıklama

# Müşteri 1: 55$'a 6 numara ayakkabı satın aldı.

# Müşteri 2: 45$'a 6 numara ayakkabı satın aldı.

# Müşteri 3: Boyut 6 artık mevcut değil, bu nedenle satın alma yok.


# Müşteri 4: 4 numara ayakkabıyı 40$'a satın aldı.

# Müşteri 5: 18 numara ayakkabıyı 60 dolara satın aldı.

# Müşteri 6: Boyut 10 mevcut değil, bu nedenle satın alma yok.

# Kazanılan toplam para = 55 + 45 + 40 + 60 = 200 $

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
numShoes = int(input())
shoes = Counter(map(int, input().split()))
numCust = int(input())
income = 0
for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1
print(income)