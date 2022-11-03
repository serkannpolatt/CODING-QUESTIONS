# Problem
# Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard’s 0 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

# Write a query calculating the amount of error (i.e. actual – miscalculated:  average monthly salaries), and round it up to the next integer.

# Input Format
# The EMPLOYEES table is described as follows:

# Column	Type
# ID	Integer
# Name	String
# Salary	Integer
# Note: Salary is per month.

#---------------------------------------------

# Sorun
# Samantha, ÇALIŞANLAR tablosundaki tüm çalışanların aylık ortalama maaşlarını hesaplamakla görevlendirildi, ancak hesaplamayı tamamlayana kadar klavyesinin 0 tuşunun bozulduğunu fark etmedi. Yanlış hesaplaması (sıfırları çıkarılmış maaşları kullanarak) ile gerçek ortalama maaş arasındaki farkı bulmak için yardımınızı istiyor.

# Hata miktarını hesaplayan bir sorgu yazın (yani gerçek - yanlış hesaplanmış: ortalama aylık maaşlar) ve bir sonraki tam sayıya yuvarlayın.

# Giriş Formatı
# ÇALIŞANLAR tablosu şu şekilde açıklanmıştır:

# Sütun Türü
# Kimlik Tam Sayısı
# İsim Dizesi
# Maaş Tam Sayısı
# Not: Maaş aylıktır.

SELECT CEIL(AVG(Salary)-AVG(REPLACE(Salary,'0','')))
FROM  EMPLOYEES