# Problem
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format
# The first line of input contains the original string. The next line contains the substring.

# Constraints
# 1 <= len(string) <= 200
# Each character in the string is an ascii character.

# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.

# #------------------------------------------------------------

# Sorun
# Bu sorgulamada, kullanıcı bir dize ve bir alt dize girer. Verilen dizede alt dizenin kaç kez oluştuğunu yazdırmanız gerekir. Dize geçişi sağdan sola değil soldan sağa gerçekleşecektir.

# NOT: Dize harfleri büyük/küçük harf duyarlıdır.

# Giriş Formatı
# Girişin ilk satırı orijinal dizeyi içerir. Bir sonraki satır alt dizeyi içerir.

# kısıtlamalar
# 1 <= len(dize) <= 200
# Dizedeki her karakter bir ascii karakteridir.

# Çıkış formatı
# Orijinal dizede alt dizenin toplam oluşum sayısını gösteren tam sayıyı çıktılayın.

def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)