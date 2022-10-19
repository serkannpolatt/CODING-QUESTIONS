# Problem
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

# Input Format
# Only one line of input containing N, the size of the rangoli.

# Constraints
# 0 < N < 27

# Output Format
# Print the alphabet rangoli in the format explained above.

#-----------------------------------------------------------

# Sorun
# Size bir tamsayı verilir, N. Göreviniz, N boyutunda bir alfabe rangoli yazdırmak. (Rangoli, desenlerin oluşturulmasına dayanan bir Hint halk sanatı biçimidir.)

# Farklı boyutlarda alfabe rangoli aşağıda gösterilmiştir:

# Rangoli'nin merkezinde ilk alfabe harfi a, sınırında N. alfabe harfi bulunur (alfabetik sırayla).

# Giriş Formatı
# Rangoli'nin boyutu olan N içeren yalnızca bir giriş satırı.

# Kısıtlamalar
# 0 < N < 27

# Çıkış formatı
# Rangoli alfabesini yukarıda açıklanan biçimde yazdırın.

def print_rangoli(size):
    # your code goes here
    import string
    design = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)