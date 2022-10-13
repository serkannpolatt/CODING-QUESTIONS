# Problem
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have ‘WELCOME’ written in the center.
# The design pattern should only use |, . and – characters.

# Input Format
# A single line containing the space separated values of N and M.

# Constraints
# 5 < N < 101
# 15 < M < 303
# Output Format
# Output the design pattern.

#----------------------------------------------

# Sorun
# Bay Vincent bir paspas imalat şirketinde çalışıyor. Bir gün, aşağıdaki özelliklere sahip yeni bir paspas tasarladı:

# Mat boyutu N X M olmalıdır. (N tek bir doğal sayıdır ve M 3 çarpı N'dir.)
# Tasarımın ortasına 'HOŞ GELDİNİZ' yazılmalıdır.
# Tasarım deseni yalnızca |, kullanmalıdır. ve – karakterler.

# Giriş Formatı
# N ve M'nin boşlukla ayrılmış değerlerini içeren tek bir satır.

# Kısıtlamalar
# 5 < N < 101
# 15 < E < 303
# Çıkış formatı
# Tasarım deseninin çıktısını alın.

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
for i in range(1, N, 2):
    print((i * ".|.").center(M,"-"))
print("WELCOME".center(M, "-"))
for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-")) 