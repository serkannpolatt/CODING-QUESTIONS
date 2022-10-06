# Problem
# Given the participants’ score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

# Input Format
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.

# Constraints
# 2 ≤  n ≤  10
# -100 ≤  A[i] ≤ 100
# Output Format
# Print the runner-up score.

#---------------------------------------------------

# Sorun
# Üniversite Spor Gününüz için katılımcıların puan tablosuna bakıldığında, ikincilik puanını bulmanız gerekir. Size n puan verilir. Bunları bir listede saklayın ve ikincinin puanını bulun.

# Giriş Formatı
# İlk satırda n bulunur. İkinci satır, her biri bir boşlukla ayrılmış n tam sayıdan oluşan bir A[] dizisini içerir.

# kısıtlamalar
# 2 ≤ n ≤ 10
# -100 ≤ A[i] ≤ 100
# Çıkış formatı
# İkincilik puanını yazdırın.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])