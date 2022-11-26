# Task
# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i belongs to A, you add 1 to your happiness. If i belongs to B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Constraints
# 1 <= n <= 105
# 1 <= m <= 105
# 1 <= Any integer in the input <= 109
# Input Format
# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.

# Output Format
# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output

# 1
# Explanation


# You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.

# Hence, the total happiness is 2 – 1 = 1.

#-------------------------------------------------------------

# Görev
# Bir dizi n tamsayı vardır. Ayrıca her biri m tamsayı içeren 2 ayrık küme, A ve B vardır. A kümesindeki tüm tam sayıları seversiniz ve B kümesindeki tüm tam sayıları sevmezsiniz. İlk mutluluğunuz 0'dır. Dizideki her i tamsayısı için, eğer A'ya aitsem, mutluluğunuza 1 eklersiniz. Ben B'ye aitsem, mutluluğunuza -1 eklersiniz. Yoksa mutluluğunuz değişmez. Sonunda nihai mutluluğunuzu ortaya çıkarın.

# Not: A ve B kümeler olduğundan, tekrarlanan öğeleri yoktur. Ancak dizi yinelenen öğeler içerebilir.

# Kısıtlamalar
# 1 <= n <= 105
# 1 <= m <= 105
# 1 <= Girişteki herhangi bir tam sayı <= 109
# Giriş Formatı
# İlk satır, bir boşlukla ayrılmış n ve m tamsayılarını içerir.
# İkinci satır, dizinin elemanları olan n tamsayı içerir.
# Üçüncü ve dördüncü satırlar sırasıyla m tamsayı, A ve B içerir.

# Çıkış formatı
# Tek bir tamsayı çıktısı, toplam mutluluğunuz.

# Örnek Giriş

# 3 2
# 1 5 3
# 3 1
# 5 7
# Örnek Çıktı

# 1
# Açıklama


# A kümesindeki 3 ve 1 numaralı elemanlar için 1 birim mutluluk kazanırsınız. B kümesindeki 5 için 1 birim kaybedersiniz. B kümesindeki 7 numaralı eleman dizide olmadığı için hesaplamaya dahil edilmez.

# Böylece toplam mutluluk 2 – 1 = 1 olur.

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    
    good = set(map(int, input().strip().split(' ')))
    bad = set(map(int, input().strip().split(' ')))
    
    for i in arr:
        if i in good:
            happiness += 1
        elif i in bad:
            happiness -= 1
    print(happiness)