#  Problem
    # Given an integer, n, perform the following conditional actions:

        #If  n is odd, print Weird 
        # If n is even and in the inclusive range of 2 to 5, print Not Weird
        # If n is even and in the inclusive range of 6 to 20, print Weird
        # If n is even greater than 20, print Not Weird

# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 ≤ n ≤ 100

# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

#----------------------------------------------------------------------------------------------------------------#

#  Sorun
    # Bir tamsayı verildiğinde, n, aşağıdaki koşullu eylemleri gerçekleştirin:

        #n tek ise, Tuhaf yazdır
        # n çift ise ve 2 ile 5 arasında bir aralıktaysa, Garip Değil'i yazdırın
        # n çift ise ve 6 ile 20 arasında bir aralıktaysa, Tuhaf yazdır
        # n 20'den büyükse, Garip Değil'i yazdırın
        
# Giriş Formatı
# Pozitif bir tamsayı içeren tek bir satır, n.

# Kısıtlamalar
# 1 ≤ n ≤ 100

# Çıkış formatı
# Sayı tuhafsa Tuhaf Yazdır. Aksi takdirde, Garip Değil'i yazdırın.


n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")            