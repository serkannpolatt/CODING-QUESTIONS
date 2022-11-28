# Task
# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

# Input Format
# The first line contains integer T, the number of test cases.
# The next T lines contains the string S.

# Constraints
# 0 < T < 100
# Output Format
# Print “True” or “False” for each test case without quotes.

# Sample Input

# 2
# .*\+
# .*+
# Sample Output

# True
# False
# Explanation

# .*\+ : Valid regex.
# .*+: Has the error multiple repeat. Hence, it is invalid.

#-------------------------------------------------------------

# Görev
# Size bir S dizisi verilir.
# Göreviniz S'nin geçerli bir normal ifade olup olmadığını bulmak.

# Giriş Formatı
# İlk satır, test senaryolarının sayısı olan T tamsayısını içerir.
# Sonraki T satırları S dizesini içerir.

# Kısıtlamalar
# 0 < T < 100
# Çıkış formatı
# Her test durumu için tırnak işaretleri olmadan “Doğru” veya “Yanlış” yazdırın.

# Örnek Giriş

# 2
# .*\+
# .*+
# Örnek Çıktı

# Doğru
# Yanlış
# Açıklama

# .*\+ : Geçerli normal ifade.
# .*+: Çoklu tekrar hatası var. Dolayısıyla geçersizdir.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
T = int(input())
for _ in range(T):  
    try:
        print(bool(re.compile(input())))
    except:
        print('False')