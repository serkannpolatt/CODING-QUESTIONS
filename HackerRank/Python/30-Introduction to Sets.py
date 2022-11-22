# # Objective
# # A set is an unordered collection of elements without duplicate entries.

# # When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

# # Basically, sets are used for membership testing and eliminating duplicate entries.

# # Task
# # Now, let’s use our knowledge of sets and help Mickey.

# # Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# # Formula used:


# # Average = Sum of Distinct Heights / Total Number of Distinct Heights

# # Input Format
# # The first line contains the integer, N, the total number of plants.

# # The second line contains the N space separated heights of the plants.


# # Constraints
# # 0 < N <= 100

# # Output Format
# # Output the average height value on a single line.

# # Explanation

# # Here, set ([154, 161, 167, 170, 171, 174, 176, 182]) is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.

# #--------------------------------------------------------------

# # Amaç
# # Küme, yinelenen girişleri olmayan sırasız bir öğe koleksiyonudur.

# # Basıldığında, yinelendiğinde veya bir diziye dönüştürüldüğünde, öğeleri rastgele bir sırada görünecektir.

# # Temel olarak kümeler, üyelik testi ve yinelenen girişleri ortadan kaldırmak için kullanılır.

# # Görev
# # Şimdi set bilgimizi kullanalım ve Mickey'e yardım edelim.

# # Bayan Gabriel Williams, Bölge Koleji'nde botanik profesörüdür. Bir gün öğrencisi Mickey'den serasındaki farklı yüksekliklere sahip tüm bitkilerin ortalamasını hesaplamasını istedi.

## Kullanılan formül:


# # Ortalama = Farklı Yüksekliklerin Toplamı / Farklı Yüksekliklerin Toplam Sayısı

# # Giriş Formatı
# # İlk satır, toplam bitki sayısı olan N tamsayısını içerir.

# # İkinci satır, bitkilerin N boşlukla ayrılmış yüksekliklerini içerir.


# # Kısıtlamalar
# # 0 < N <= 100

# # Çıkış formatı
# # Ortalama yükseklik değerini tek bir satıra yazdırın.

# # Açıklama

# # Burada, küme ([154, 161, 167, 170, 171, 174, 176, 182]) farklı yükseklikleri içeren kümedir. sum() ve len() fonksiyonlarını kullanarak ortalamayı hesaplayabiliriz.

def average(array):
    # your code goes here
    array = set(array)
    return sum(array) / len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
