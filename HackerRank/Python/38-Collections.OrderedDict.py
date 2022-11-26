# Task
# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.

# Input Format
# The first line contains the number of items, N.
# The next N lines contains the item’s name and price, separated by a space.

# Constraints
# 0 < N <= 100
# Output Format
# Print the item_name and net_price in order of its first occurrence.

# Sample Input


# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
# Sample Output

# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20
# Explanation

# BANANA FRIES: Quantity bought: 1, Price: 12
# Net Price: 12
# POTATO CHIPS: Quantity bought: 2, Price: 30
# Net Price: 60
# APPLE JUICE: Quantity bought: 2, Price: 10
# Net Price: 20
# CANDY: Quantity bought: 4, Price: 5
# Net Price: 20

#-------------------------------------------------------------

# Görev
# Bir süpermarketin yöneticisisiniz.
# Tüketicilerin belirli bir günde satın aldıkları fiyatlarıyla birlikte N adet ürün listeniz var.
# Göreviniz, her bir item_name ve net_price ilk ortaya çıkış sırasına göre yazdırmak.
# item_name = Öğenin adı.
# net_price = Satılan ürünün miktarı ile her bir ürünün fiyatının çarpımı.

# Giriş Formatı
# İlk satır, öğe sayısını içerir, N.
# Sonraki N satır, bir boşlukla ayrılmış olarak öğenin adını ve fiyatını içerir.

# Kısıtlamalar
# 0 < N <= 100
# Çıkış formatı
# item_name ve net_price ilk geçtiği sıraya göre yazdırın.

# Örnek Giriş


# 9
# MUZ KIZARTMASI 12
# PATATES CİPS 30
# ELMA SUYU 10
# ŞEKER 5
# ELMA SUYU 10
# ŞEKER 5
# ŞEKER 5
# ŞEKER 5
# PATATES CİPS 30
# Örnek Çıktı

# MUZ KIZARTMASI 12
# PATATES CİPS 60
# ELMA SUYU 20
# ŞEKER 20
# Açıklama

# MUZ KIZARTMASI: Satın alınan miktar: 1, Fiyat: 12
# Net Fiyat: 12
# PATATES CİPS: Satın alınan miktar: 2, Fiyat: 30
# Net Fiyat: 60
# ELMA SUYU: Satın alınan miktar: 2, Fiyat: 10
# Net Fiyat: 20
# ŞEKER: Satın alınan miktar: 4, Fiyat: 5
# Net Fiyat: 20

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

order = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    order[item] = order.get(item, 0) + int(price)
for item, price in order.items():
    print(item, price)