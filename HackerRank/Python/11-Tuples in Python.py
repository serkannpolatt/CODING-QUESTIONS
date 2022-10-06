# Task
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format
# The first line contains an integer, n, denoting the number of elements in the tuple.

# The second line contains n space-separated integers describing the elements in tuple t.

#----------------------------------------------

# Görev
# Girdi olarak bir tamsayı,&nbsp;n&nbsp;ve&nbsp;n&nbsp;boşlukla ayrılmış tamsayılar verildiğinde, bu n&nbsp;tamsayıların bir demetini (t) oluşturun. Ardından hash(t) sonucunu hesaplayın ve yazdırın.

# Not:&nbsp;hash(), __builtins__ modülündeki işlevlerden biridir, dolayısıyla içe aktarılması gerekmez.

# Giriş Formatı
# İlk satır, tanımlama grubundaki öğelerin sayısını belirten bir n tamsayısını içerir.

# İkinci satır, t demetindeki öğeleri açıklayan boşlukla ayrılmış n tamsayı içerir.

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))