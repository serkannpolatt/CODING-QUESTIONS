# Problem
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

    # The year can be evenly divided by 4, is a leap year, unless:
    # The year can be evenly divided by 100, it is NOT a leap year, unless:
    # The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. 

# Task
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# Input Format
# Read year, the year to test.

# Constraints
# 1900 <= year <= 10^5


# Output Format
# The function must return a Boolean value (True/False). Output is handled by the provided code stub.

#----------------------------------------------------------------------------------------------------

# Sorun
# 29 Şubat olarak neredeyse her dört yılda bir takvime fazladan bir gün eklenir ve bu güne artık gün denir. Gezegenimizin güneş etrafında dönmesinin yaklaşık 365,25 gün sürdüğü gerçeği için takvimi düzeltir. Artık yıl, artık gün içerir.

# Gregoryen takviminde artık yılları belirlemek için üç koşul kullanılır:

    # Yıl 4'e eşit olarak bölünebilir, şu durumlar dışında artık yıldır:
    # Yıl 100'e eşit olarak bölünebilir, aşağıdaki durumlar dışında artık yıl DEĞİLDİR:
    # Yıl da 400'e tam bölünür. O zaman artık yıldır.
# Bu, Gregoryen takviminde 2000 ve 2400 yıllarının artık yıl olduğu, 1800, 1900, 2100, 2200, 2300 ve 2500 yıllarının artık yıl DEĞİL olduğu anlamına gelir.

# Görev
# Bir yıl verildiğinde artık yıl olup olmadığını belirleyin. Artık yıl ise, Boolean True değerini döndürün, aksi takdirde False döndürün.

# Sağlanan kod saplamasının STDIN'den okuduğunu ve argümanları is_leap işlevine ilettiğini unutmayın. Yalnızca is_leap işlevini tamamlamak gerekir.

# Giriş Formatı
# Yılı, test edilecek yılı okuyun.

# Kısıtlamalar
# 1900 <= yıl <= 10^5


# Çıkış formatı
# İşlev bir Boole değeri (Doğru/Yanlış) döndürmelidir. Çıktı, sağlanan kod saplaması tarafından işlenir.


def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return leap
    if (year % 4 == 0):
        return True
    else:
        return False  
    
    return leap
year = int(input())
print(is_leap(year))