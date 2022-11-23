# Task
# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

# Input Format
# The first line contains T, the number of testcases.
# Each testcase contains 2 lines, representing time t1 and time t2.

# Constraints
# Input contains only valid timestamps
# year <= 3000.
# Output Format
# Print the absolute difference (t1 – t2) in seconds.

#-------------------------------------------------------------

# Görev
# Kullanıcılar sosyal medyada URL, resim, durum güncellemesi vb. gibi bir güncelleme yayınladığında, ağlarındaki diğer kullanıcılar bu yeni gönderiyi haber akışlarında görebilirler. Kullanıcılar ayrıca gönderinin tam olarak ne zaman yayınlandığını, yani kaç saat, dakika veya saniye önce olduğunu görebilir.

# Bazen gönderiler farklı saat dilimlerinde yayınlanıp görüntülendiğinden, bu kafa karıştırıcı olabilir. Bir kullanıcının haber akışında aşağıdaki biçimde görebileceği böyle bir gönderi için size iki zaman damgası verilir:

# Gün gg Pzt yyyy ss:dd:ss +xxxx

# Burada +xxxx saat dilimini temsil eder. Göreviniz, aralarındaki mutlak farkı (saniye cinsinden) yazdırmaktır.

# Giriş Formatı
# İlk satır, test çantası sayısı olan T'yi içerir.
# Her test çantası, t1 zamanını ve t2 zamanını temsil eden 2 satır içerir.

# Kısıtlamalar
# Girdi yalnızca geçerli zaman damgalarını içerir
# yıl <= 3000.
# Çıkış formatı
# Mutlak farkı (t1 – t2) saniye cinsinden yazdırın.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
from datetime import datetime
def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs((t1-t2).total_seconds()))) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()