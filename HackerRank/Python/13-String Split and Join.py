# Task
# You are given a string. Split the string on a ” ” (space) delimiter and join using a – hyphen.

# Input Format
# The first line contains a string consisting of space separated words.

# Output Format
# Print the formatted string as explained above.

# Görev
# Size bir dize verilir. Dizeyi bir ” ” (boşluk) sınırlayıcısına ayırın ve bir – tire kullanarak birleştirin.

# Giriş Formatı
# İlk satır, boşlukla ayrılmış sözcüklerden oluşan bir dize içerir.

# Çıkış formatı
# Biçimlendirilmiş dizeyi yukarıda açıklandığı gibi yazdırın.

def split_and_join(line):
    # write your code here
    line = line.split()
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)