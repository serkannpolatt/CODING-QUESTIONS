# Problem
# Consider the following:

# A string, s, of length n where s = c0c1. . . . cn-1.

# An integer, k, where k is a factor of n.

# We can split s into n/k substrings where each subtring, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

# The characters in ui are a subsequence of the characters in ti.

# Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. In other words, if the character at some index j in ti occurs at a previous index < j in ti, then do not include the character in string ui.

# Given s and k, print n/k lines where each line i denotes string ui.

# Example

# s = “AAABCADDE”

# k = 3

# There are three substrings of length 3 to consider: ‘AAA’, ‘BCA’ and ‘DDE’. The first substring is all ‘A’ characters, so u1 = ‘A’. The second substring has all distinct characters, so u2 = ‘BCA’. The third substring has 2 different characters, so u3 = ‘DE’. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

# Function Description 
# Complete the merge_the_tools function in the editor below.

# merge_the_tools has the following parameters:

# string s: the string to analyze
# int k: the size of substrings to analyze
# Prints
# Print each subsequence on a new line. There will be n/k of them. No return value is expected.

# Input Format
# The first line contains a single string, s.

# The second line contains an integer, k, the length of each substring.

# Constraints
# 1 <= n <= 10^4, where n is the length of s
# 1 <= k <= n 
# It is guaranteed that n is a multiple of k.

# Explanation 

# Split s into n/k = 9/3 = 3 equal parts of length k = 3. Convert each ti to ui by removing any subsequent occurrences of non-distinct characters in ti:

# t0 = “AAB” – u0 = “AB”
# t1 = “CAA” – u1 = “CA”
# t2 = “ADA” – u2 = “AD”
# Print each ui on a new line.

#---------------------------------------------------

# Sorun
# Aşağıdakileri göz önünde bulundur:

# n uzunluğunda bir dize, s, burada s = c0c1. . . . cn-1.

# Bir tamsayı, k, burada k, n'nin bir faktörüdür.

# s'yi n/k alt dizgilerine bölebiliriz, burada her bir alt dizge, ti, s'deki bitişik bir k karakter bloğundan oluşur. Ardından, ui dizesini oluşturmak için her ti'yi kullanın:

# ui'deki karakterler, ti'deki karakterlerin bir devamıdır.

# Bir karakterin herhangi bir tekrarı, ui'deki her karakter tam olarak bir kez olacak şekilde dizeden kaldırılır. Başka bir deyişle, j in ti dizinindeki karakter önceki < j in ti dizininde yer alıyorsa, karakteri ui dizesine dahil etmeyin.

# Verilen s ve k, n/k satırları yazdırın, burada i her satırı ui dizesini gösterir.

# Örnek

# s = “AAABCADDE”

#k = 3

# Dikkate alınması gereken 3 uzunluğunda üç alt dizi vardır: "AAA", "BCA" ve "DDE". İlk alt dizenin tamamı 'A' karakterleridir, yani u1 = 'A'. İkinci alt dizenin tüm farklı karakterleri vardır, bu nedenle u2 = 'BCA'. Üçüncü alt dize 2 farklı karaktere sahiptir, bu nedenle u3 = 'DE'. Bir alt dizinin, karşılaşılan karakterlerin orijinal sırasını koruduğunu unutmayın. Gösterilen her alt dizideki karakterlerin sırası önemlidir.

# İşlev Açıklaması
# Aşağıdaki düzenleyicide merge_the_tools işlevini tamamlayın.

# merge_the_tools aşağıdaki parametrelere sahiptir:

# string s: analiz edilecek string
# int k: analiz edilecek alt dizelerin boyutu
# Baskılar
# Her bir sırayı yeni bir satıra yazdır. Onlardan n/k olacak. Herhangi bir dönüş değeri beklenmemektedir.

# Giriş Formatı
# İlk satır tek bir dize içerir, s.

# İkinci satır, her alt dizenin uzunluğu olan bir k tamsayısını içerir.

# Kısıtlamalar
# 1 <= n <= 10^4, burada n, s'nin uzunluğudur
# 1 <= k <= n
# n'nin k'nin katı olduğu garanti edilir.

# Açıklama

# s'yi n/k = 9/3 = k = 3 uzunluğunda 3 eşit parçaya bölün.

# t0 = “AAB” – u0 = “AB”
# t1 = “CAA” – u1 = “CA”
# t2 = “ADA” – u2 = “AD”
# Her kullanıcı arabirimini yeni bir satıra yazdırın.

def merge_the_tools(string, k):
    # your code goes here
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print (''.join(temp))
            temp = []
            len_temp = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)