# Objective
# In Python, a string of text can be aligned left, right and center.

# .ljust(width)

# This method returns a left aligned string of length width.

# .center(width)

# This method returns a centered string of length width.

# .rjust(width)

# This method returns a right aligned string of length width.

# Task
# You are given a partial code that is used for generating the HackerRank Logo of variable thickness. Your task is to replace the blank (______) with rjust, ljust or center.

# Input Format
# A single line containing the thickness value for the logo.

# Constraints
# 0 < thickness < 50


# Output Format
# Output the desired logo.

#---------------------------------------------------------------

# Amaç
# Python'da bir metin dizisi sola, sağa ve ortaya hizalanabilir.

# .ljust(genişlik)

# Bu yöntem, uzunluk genişliğinin sola hizalanmış bir dizesini döndürür.

# .center(genişlik)

# Bu yöntem, ortalanmış bir uzunluk genişliği dizesi döndürür.

# .rjust(genişlik)

# Bu yöntem, sağa hizalanmış bir uzunluk genişliği dizesi döndürür.

# Görev
# Değişken kalınlıkta HackerRank Logosunu oluşturmak için kullanılan kısmi bir kod verilir. Göreviniz boşluğu (______) rjust, ljust veya center ile değiştirmektir.

# Giriş Formatı
# Logonun kalınlık değerini içeren tek bir satır.

# Kısıtlamalar
# 0 < kalınlık < 50


# Çıkış formatı
# İstenilen logonun çıktısını alın.

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))