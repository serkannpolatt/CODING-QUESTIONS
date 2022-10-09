# Objective
# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# str.isalnum()

# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

# str.isalpha()

# This method checks if all the characters of a string are alphabetical (a-z and A-Z).

# str.isdigit()

# This method checks if all the characters of a string are digits (0-9).

# str.islower()

# This method checks if all the characters of a string are lowercase characters (a-z).

# str.isupper()


# This method checks if all the characters of a string are uppercase characters (A-Z).

# Task
# You are given a string S.

# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


# Input Format
# A single line containing a string S.

# Constraints
# 0 < len(S) < 1000

# Output Format
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

#---------------------------------------------------------------

# Amaç
# Python, temel veriler için yerleşik dize doğrulama yöntemlerine sahiptir. Bir dizenin alfabetik karakterlerden, alfanümerik karakterlerden, rakamlardan vb. oluşup oluşmadığını kontrol edebilir.

# str.isalnum()

# Bu yöntem, bir dizenin tüm karakterlerinin alfasayısal (a-z, A-Z ve 0-9) olup olmadığını kontrol eder.

# str.isalpha()

# Bu yöntem, bir dizenin tüm karakterlerinin alfabetik (a-z ve A-Z) olup olmadığını kontrol eder.

# str.isdigit()

# Bu yöntem, bir dizenin tüm karakterlerinin rakam (0-9) olup olmadığını kontrol eder.

# str.islower()

# Bu yöntem, bir dizenin tüm karakterlerinin küçük harfli karakterler (a-z) olup olmadığını kontrol eder.

# str.isupper()


# Bu yöntem, bir dizenin tüm karakterlerinin büyük harfli karakterler (A-Z) olup olmadığını kontrol eder.

# Görev
# Size bir S dizisi verilir.

# Göreviniz, S dizisinin şunları içerip içermediğini bulmaktır: alfasayısal karakterler, alfabetik karakterler, rakamlar, küçük harf ve büyük harf karakterleri.


# Giriş Formatı
# S dizesini içeren tek bir satır.

# Kısıtlamalar
# 0 < mercek(S) < 1000

# Çıkış formatı
# İlk satırda, S'nin alfanümerik karakterleri varsa True yazdırın. Aksi takdirde, Yanlış yazdırın.
# İkinci satırda, S'nin alfabetik karakterleri varsa True yazdırın. Aksi takdirde, Yanlış yazdırın.
# Üçüncü satırda, S'nin herhangi bir rakamı varsa True yazdırın. Aksi takdirde, Yanlış yazdırın.
# Dördüncü satırda, S'de küçük harf varsa True yazdırın. Aksi takdirde, Yanlış yazdırın.
# Beşinci satırda, S'de büyük harf varsa True yazdırın. Aksi takdirde, Yanlış yazdırın.

if __name__ == '__main__':
    s = input()
    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))