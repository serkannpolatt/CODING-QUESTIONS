# Problem
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Input Format
# The first line contains the first name, and the second line contains the last name.

# Constraints
# The length of the first and last name ≤ 10.

# Output Format
# Print the output as mentioned above.

#-------------------------------------------------- 

# Sorun
# Size iki farklı satırda bir kişinin adı ve soyadı verilir. Göreviniz bunları okumak ve aşağıdakileri yazdırmak:

# Giriş Formatı
# İlk satır ilk adı, ikinci satır soyadını içerir.

# Kısıtlamalar
# Adın ve soyadının uzunluğu ≤ 10.

# Çıkış formatı
# Çıktıyı yukarıda belirtildiği gibi yazdırın.

def print_full_name(a, b):
    print("Hello " + a, b + "! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)