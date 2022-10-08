# Problem
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# Input Format
# A single line containing a string S.

# Constraints
# 0 <= len(S) <= 1000

# Output Format
# Print the modified string S.

#-----------------------------------------------------------

# Sorun
# Size bir ip verilir ve göreviniz kasaları değiştirmektir. Başka bir deyişle, tüm küçük harfleri büyük harflere veya tam tersine dönüştürün.
# Giriş Formatı
# S dizesini içeren tek bir satır.

# Kısıtlamalar
# 0 <= len(S) <= 1000

# Çıkış formatı
# Değiştirilen S dizisini yazdırın.

def swap_case(s):
    num = ""
    for let in s:
        if let.isupper() == True:
            num+=(let.lower())
        else:
            num+=(let.upper())
    return num
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)