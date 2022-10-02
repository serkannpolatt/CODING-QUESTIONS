#Task
#The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

    #The first line contains the sum of two numbers.
    #The second line contains the difference of the two numbers (first – second).
    #The third line contains the product of two numbers. 

# Input Format
# The first line contains the first integer, a.
# The second line contains the second integer, b.

# Constraints
# 1 ≤ a ≤ 1010
# 1 ≤ b ≤ 1010


# Output Format
# Print the three lines as explained above.

#-------------------------------------------------------------------------------------------------------#

#Görev
#Sağlanan kod saplaması, STDIN, a ve b'den iki tamsayı okur. Üç satırı yazdırmak için kod ekleyin:

    #İlk satır iki sayının toplamını içerir.
    #İkinci satır, iki sayının farkını içerir (birinci – ikinci).
    #Üçüncü satır iki sayının çarpımını içerir.

# Giriş Formatı
# İlk satır ilk tamsayıyı içerir, a.
# İkinci satır, ikinci tamsayı b'yi içerir.

# Kısıtlamalar
# 1 ≤ bir ≤ 1010
# 1 ≤ b ≤ 1010


# Çıkış formatı
# Yukarıda açıklandığı gibi üç satırı yazdırın.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)