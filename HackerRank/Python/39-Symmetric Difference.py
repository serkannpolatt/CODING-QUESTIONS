# Task
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input Format
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format
# Output the symmetric difference integers in ascending order, one per line.

# Sample Input


# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
# Sample Output

# 5
# 9
# 11
# 12

#-------------------------------------------------------------

# Görev
# Verilen 2 tam sayı kümesi, M ve N, simetrik farklarını artan sırada yazdırın. Simetrik fark terimi, M veya N'de bulunan ancak her ikisinde de bulunmayan değerleri belirtir.

# Giriş Formatı
# Girişin ilk satırı M tamsayısını içerir.
# İkinci satır M boşlukla ayrılmış tamsayı içerir.
# Üçüncü satır N tamsayısını içerir.
# Dördüncü satır N tane boşlukla ayrılmış tamsayı içerir.

# Çıkış formatı
# Simetrik fark tamsayılarını, satır başına bir tane olacak şekilde artan sırada çıktılayın.

# Örnek Giriş


# STDIN İşlevi
# ----- --------
# 4 bir beden ayarla M = 4
# 2 4 5 9 a = {2, 4, 5, 9}
# 4 takım b beden N = 4
# 2 4 11 12 b = {2, 4, 11, 12}
# Örnek Çıktı

# 5
# 9
# 11
# 12

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    M = int(input().strip())
    set_m = set(map(int, input().strip().split(' ')))
    
    N = int(input().strip())
    set_n = set(map(int, input().strip().split(' ')))
    
    for j in sorted(set_m ^ set_n):
        print(j)