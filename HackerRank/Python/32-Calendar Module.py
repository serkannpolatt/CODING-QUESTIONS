# Objective
# The calendar module allows you to output calendars and provides additional useful functions for them.

# class calendar.TextCalendar([firstweekday])

# This class can be used to generate plain text calendars.

# Task
# You are given a date. Your task is to find what the day is on that date.

# Input Format
# A single line of input containing the space separated month, day and year, respectively, in  MM DD YYYY  format.

# Constraints
# 2000 < year < 3000

# Output Format
# Output the correct day in capital letters.

#-------------------------------------------------------------

# Amaç
# Takvim modülü, takvimlerin çıktısını almanıza olanak tanır ve onlar için ek kullanışlı işlevler sağlar.

# sınıf takvim.TextCalendar([ilk hafta içi])

# Bu sınıf, düz metin takvimleri oluşturmak için kullanılabilir.

# Görev
# Size bir tarih verilir. Senin görevin o tarihte günün ne olduğunu bulmak.

# Giriş Formatı
# Ay, gün ve yılı sırasıyla AA GG YYYY biçiminde boşlukla içeren tek bir girdi satırı.

# Kısıtlamalar
# 2000 < yıl < 3000

# Çıkış formatı
# Doğru günü büyük harflerle yazdırın.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())