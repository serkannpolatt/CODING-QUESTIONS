# Task
# The provided code stub read two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

# No rounding or formatting is necessary.

# Input Format
# The first line contains the first integer, a.

# The second line contains the second integer, b.

# Output Format
# Print the two lines as described above.

#------------------------------------------------

# Görev
# Sağlanan kod saplaması, STDIN'den iki tamsayıyı, a ve b'yi okudu.

# İki satır yazdırmak için mantık ekleyin. İlk satır, tamsayı bölümünün sonucunu içermelidir, a // b. İkinci satır, kayan noktalı bölmenin sonucunu, a / b içermelidir.

# Yuvarlama veya biçimlendirme gerekmez.

# Giriş Formatı
# İlk satır ilk tamsayıyı içerir, a.

# İkinci satır, ikinci tamsayı b'yi içerir.

# Çıkış formatı
# Yukarıda açıklandığı gibi iki satırı yazdırın.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)