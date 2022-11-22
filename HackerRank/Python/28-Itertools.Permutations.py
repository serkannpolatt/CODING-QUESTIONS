# Objective
# This tool returns successive r length permutations of elements in an iterable.

# If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.

# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

# Task
# You are given a string S.

# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

# Input Format
# A single line containing the space separated string S and the integer value k.


# Constraints
# 0 < k <= len(S)
# The string contains only UPPERCASE characters.

# Output Format
# Print the permutations of the string S on separate lines.

# Explanation

# All possible size 2 permutations of the string “HACK” are printed in lexicographic sorted order.

#---------------------------------------------------

# Amaç
# Bu araç, yinelenebilir bir öğedeki ardışık r uzunluk permütasyonlarını döndürür.

# r belirtilmemişse veya Yok ise, o zaman r yinelenebilirin uzunluğunu varsayılan olarak alır ve tüm olası tam uzunluk permütasyonları oluşturulur.

# Permütasyonlar sözlükbilimsel olarak sıralanmış bir düzende yazdırılır. Bu nedenle, yinelenebilir girdi sıralanırsa, permütasyon demetleri sıralı bir düzende üretilecektir.

# Görev
# Size bir S dizisi verilir.

# Göreviniz, dizgenin k boyutundaki tüm olası permütasyonları sözlükbilimsel olarak sıralanmış bir sırayla yazdırmaktır.

# Giriş Formatı
# Boşlukla ayrılmış S dizesini ve k tamsayı değerini içeren tek bir satır.


# Kısıtlamalar
# 0 < k <= len(S)
# Dize yalnızca BÜYÜK HARF karakterleri içerir.

# Çıkış formatı
# S dizisinin permütasyonlarını ayrı satırlara yazdırın.

# Açıklama

# “HACK” dizisinin tüm olası 2. boyut permütasyonları sözlükbilimsel olarak sıralanmış sırada yazdırılır.

from itertools import permutations
string, length = input().split()
output = ["".join(i) for i in permutations(string,int(length))]
output.sort()
print("\n".join(output))