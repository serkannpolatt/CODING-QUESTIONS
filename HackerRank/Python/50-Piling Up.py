# Task
# There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if cube[i] is on top of cube[j] then sideLength|j| => sideLength|i|.

# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

# Example

# blocks = [1, 2, 3, 8, 7]

# Result: No

# After choosing the rightmost element, 7, choose the leftmost element, 1. After than, the choices are 2 and 8. These are both larger than the top block of size 1.

# blocks = [1, 2, 3, 7, 8]


# Result: Yes

# Choose blocks from right to left in order to successfully stack the blocks.

# Input Format
# The first line contains a single integer T, the number of test cases.
# For each test case, there are 2 lines.
# The first line of each test case contains n, the number of cubes.
# The second line contains n space separated integers, denoting the sideLengths of each cube in that order.


# Constraints
# 1 <= T <= 5
# 1 <= n <= 105
# 1 <= sideLength < 231
# Output Format
# For each test case, output a single line containing either Yes or No.

# Sample Input

# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]
# Sample Output


# Yes
# No
# Explanation

# In the first test case, pick in this order: left – 4, right – 4, left – 3, right – 3, left – 2, right – 1.
# In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.

#-------------------------------------------------------------

# Görev
# Yatay bir sıra n küp var. Her bir küpün uzunluğu verilmiştir. Yeni bir dikey küp yığını oluşturmanız gerekiyor. Yeni yığın şu yönergeleri izlemelidir: eğer [i] küpü[j] küpünün üzerindeyse yanUzunluk|j| => yanUzunluk|i|.

# Küpleri istiflerken, her seferinde yalnızca en soldaki veya en sağdaki küpü alabilirsiniz. Küpleri istiflemek mümkünse Evet'i yazdırın. Aksi takdirde, No yazdırın.

# Örnek

# blok = [1, 2, 3, 8, 7]

# Sonuç: Hayır

# En sağdaki eleman olan 7'yi seçtikten sonra, en soldaki elemanı seçin, 1'den sonra, seçenekler 2 ve 8'dir. Bunların ikisi de boyut 1'in üst bloğundan daha büyüktür.

# blok = [1, 2, 3, 7, 8]


# Sonuç: Evet

# Blokları başarılı bir şekilde istiflemek için blokları sağdan sola doğru seçin.

# Giriş Formatı
# İlk satır, test senaryolarının sayısı olan tek bir T tamsayısını içerir.
# Her test durumu için 2 satır vardır.
# Her test durumunun ilk satırı, küp sayısı olan n'yi içerir.
# İkinci satır, bu sırayla her bir küpün yan uzunluklarını gösteren, boşlukla ayrılmış n tamsayı içerir.


# Kısıtlamalar
# 1 <= T <= 5
# 1 <= n <= 105
# 1 <= yan uzunluk < 231
# Çıkış formatı
# Her test durumu için, Evet veya Hayır içeren tek bir satır çıktısı alın.

# Örnek Giriş

# STDIN İşlevi
# ----- --------
# 2 T = 2
# 6 blok[] boyut n = 6
# 4 3 2 1 3 4 blok = [4, 3, 2, 1, 3, 4]
# 3 blok[] boyut n = 3
# 1 3 2 blok = [1, 3, 2]
# Örnek Çıktı


# Evet
# Numara
# Açıklama

# İlk test durumunda, şu sırayla seçim yapın: sol – 4, sağ – 4, sol – 3, sağ – 3, sol – 2, sağ – 1.
# İkinci test durumunda, hiçbir sıra dikey küplerin uygun bir düzenini vermez. 3 her zaman 1 veya 2'den sonra gelir.


# Enter your code here. Read input from STDIN. Print output to STDOUT
ANS = []
T = int(input())

for _ in range(T):
    n = int(input())
    sl = list(map(int, input().split()))

    for _ in range(n-1):
        if sl[0] >= sl[len(sl)-1]:
            a = sl[0]
            sl.pop(0)
        elif sl[0] < sl[len(sl)-1]:
            a = sl[len(sl)-1]
            sl.pop(len(sl)-1)
        else:
            pass

        if len(sl) == 1:
            ANS.append("Yes")

        if((sl[0] > a) or (sl[len(sl)-1] > a)):
            ANS.append("No")
            break

print("\n".join(ANS))