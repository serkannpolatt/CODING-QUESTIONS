# Problem
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# Let’s try to understand this with an example.
# You are given an immutable string, and you want to make changes to it.

# Task
# Read a given string, change the character at a given index and then print the modified string.


# Input Format
# The first line contains a string, S.

# The next line contains an integer i, denoting the index location and a character c separated by a space.

# Output Format
# Using any of the methods explained above, replace the character at index i with character c.

#------------------------------------------------------------

# Sorun
# Listelerin değişken olduğunu (değiştirilebilirler) ve demetlerin değişmez olduğunu (değiştirilemezler) gördük.
# Bunu bir örnekle anlamaya çalışalım.
# Size değişmez bir dizi verildi ve siz onda değişiklik yapmak istiyorsunuz.

# Görev
# Verilen bir diziyi okuyun, verilen bir dizindeki karakteri değiştirin ve sonra değiştirilen diziyi yazdırın.


# Giriş Formatı
# İlk satırda bir dize var, S.

# Sonraki satır, dizin konumunu belirten bir i tamsayısı ve bir boşlukla ayrılmış bir c karakteri içerir.

# Çıkış formatı
# Yukarıda açıklanan yöntemlerden herhangi birini kullanarak i dizinindeki karakteri c karakteriyle değiştirin.

def mutate_string(string, position, character):
    n = list(string)
    n[position] = character
    string = "".join(n)
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)