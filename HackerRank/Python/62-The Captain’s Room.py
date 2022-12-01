# Task
# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1.

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain’s room.

# Mr. Anant needs you to help him find the Captain’s room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of K and the room number list.

# Input Format
# The first line consists of an integer, K, the size of each group.
# The second line contains the unordered elements of the room number list.

# Constraints
# 1 < K < 1000
# Output Format
# Output the Captain’s room number.


# Sample Input

# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
# Sample Output

# 8
# Explanation


# The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times except for room number 8.
# Hence, 8 is the Captain’s room number.

#-------------------------------------------------------------

# Görev
# Bay Anant Asankhya, INFINITE otelinin yöneticisidir. Otelde sonsuz sayıda oda bulunmaktadır.

# Güzel bir gün, sınırlı sayıda turist otelde kalmaya gelir.
# Turistler şunlardan oluşur:
# → Bir Kaptan.
# → K ≠ 1 olmak üzere grup başına K üyeden oluşan bilinmeyen bir aile grubu.

# Kaptana ayrı bir oda, geri kalanına grup başına bir oda verildi.

# Bay Anant'ın rastgele düzenlenmiş oda girişlerinin sırasız bir listesi var. Liste, tüm turistlerin oda numaralarından oluşmaktadır. Oda numaraları, Kaptan'ın odası hariç, grup başına K kez görünecektir.

# Bay Anant'ın Kaptan'ın oda numarasını bulması için sana ihtiyacı var.
# Toplam turist sayısı veya toplam aile grubu sayısı sizin tarafınızdan bilinmiyor.
# Sadece K değerini ve oda numarası listesini biliyorsunuz.

# Giriş Formatı
# İlk satır, her grubun boyutu olan bir K tamsayısından oluşur.
# İkinci satır, oda numarası listesinin sırasız öğelerini içerir.

# Kısıtlamalar
# 1 < K < 1000
# Çıkış formatı
# Kaptanın oda numarasını çıkar.


# Örnek Giriş

# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# Örnek Çıktı

# 8
# Açıklama


# Oda numaralarının listesi 31 eleman içerir. K 5 olduğundan, 6 aile grubu olmalıdır. Verilen listede 8 numaralı oda hariç tüm numaralar 5 kez tekrarlanır.
# Dolayısıyla 8, Kaptanın oda numarasıdır.


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
ROOM_LIST = input().split()
ROOM_SET = set(ROOM_LIST)

for ele in list(ROOM_SET):
    ROOM_LIST.remove(ele)

CAPTAIN_ROOM_NUM = ROOM_SET.difference(set(ROOM_LIST)).pop()
print(CAPTAIN_ROOM_NUM)