# Problem
# We define an employee’s total earnings to be their monthly salary x months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as 2 space-separated integers.

# Input Format
# The Employee table containing employee data for a company is described as follows:

# Column	Type
# employee_id	Integer
# name	String
# months	Integer
# salary	Integer
# where employee_id is an employee’s ID number, name is their name, months is the total number of months they’ve been working for the company, and salary is the their monthly salary.

# Sample Input

# employee_id	name	months	salary
# 12228	Rose	15	1968
# 33645	Angela	1	3443
# 45692	Frank	17	1608
# 56118	Patrick	7	1345
# 59725	Lisa	11	2330
# 74197	Kimberly	16	4372
# 78454	Bonnie	8	1771
# 83565	Michael	6	2017
# 98607	Todd	5	3396
# 99989	Joe	9	3573
# Sample Output

# 69952 1
# Explanation
# The table and earnings data is depicted in the following diagram:

# employee_id	name	months	salary	earnings
# 12228	Rose	15	1968	29520
# 33645	Angela	1	3443	3443
# 45692	Frank	17	1608	27336
# 56118	Patrick	7	1345	9415
# 59725	Lisa	11	2330	25630
# 74197	Kimberly	16	4372	69952
# 78454	Bonnie	8	1771	14168
# 83565	Michael	6	2017	12102
# 98607	Todd	5	3396	16980
# 99989	Joe	9	3573	32157
# The maximum earnings value is 69952. The only employee with earnings=69952  is Kimberly, so we print the maximum earnings value (69952) and a count of the number of employees who have earned $69952 (which is 1) as two space-separated values.

#------------------------------------------------

# Sorun
# Çalışan tablosunda bir çalışanın toplam kazancını aylık maaşı x çalışılan ay olarak ve maksimum toplam kazancı, herhangi bir çalışan için maksimum toplam kazanç olarak tanımlarız. Tüm çalışanlar için maksimum toplam kazancı ve maksimum toplam kazancı olan toplam çalışan sayısını bulmak için bir sorgu yazın. Ardından bu değerleri boşlukla ayrılmış 2 tam sayı olarak yazdırın.

# Giriş Formatı
# Bir şirket için çalışan verilerini içeren Çalışan tablosu aşağıdaki gibi tanımlanır:

# Sütun Türü
# çalışan_kimliği Tamsayı
# isim Dize
# ay Tamsayı
# maaş Tamsayı
# burada çalışan_kimliği bir çalışanın kimlik numarası, adı adı, aylar şirkette çalıştıkları toplam ay sayısı ve maaş aylık maaşlarıdır.

# Örnek Giriş

# çalışan_kimliği adı ay maaşı
# 12228 Gül 15 1968
# 33645 Angela 1 3443
# 45692 Frank 17 1608
# 56118 Patrick 7 1345
# 59725 Lisa 11 2330
# 74197 Kimberly 16 4372
# 78454 Bonnie 8 1771
# 83565 Michael 6 2017
# 98607 Todd 5 3396
# 99989 Joe 9 3573
# Örnek Çıktı

# 69952 1
# Açıklama
# Tablo ve kazanç verileri aşağıdaki şemada gösterilmiştir:

# çalışan_kimliği adı ay maaş kazançları
# 12228 Gül 15 1968 29520
# 33645 Angela 1 3443 3443
# 45692 Frank 17 1608 27336
# 56118 Patrick 7 1345 9415
# 59725 Lisa 11 2330 25630
# 74197 Kimberly 16 4372 69952
# 78454 Bonnie 8 1771 14168
# 83565 Michael 6 2017 12102
# 98607 Todd 5 3396 16980
# 99989 Joe 9 3573 32157
# Maksimum kazanç değeri 69952'dir. Kazancı=69952 olan tek çalışan Kimberly'dir, bu nedenle maksimum kazanç değerini (69952) ve 69952 $ kazanan çalışan sayısını (1'dir) iki boşluklu olarak yazdırırız. değerler.

select max(months * salary), count(months * salary) 
from Employee where (months * salary) 
= (select max(months * salary) from Employee);