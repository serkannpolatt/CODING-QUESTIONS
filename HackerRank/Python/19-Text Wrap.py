# Problem
# You are given a string S and width w.

# Your task is to wrap the string into a paragraph of width w.

# Input Format
# The first line contains a string, S.

# The second line contains the width, w.

# Constraints
# 0 < len(S) < 1000
# 0 < w < len(S)
# Output Format
# Print the text wrapped paragraph.

#---------------------------------------------------------------

# Sorun
# Size bir S dizisi ve w genişliği verilir.

# Göreviniz, dizeyi w genişliğinde bir paragrafa sarmak.

# Giriş Formatı
# İlk satır bir dize içerir, S.

# İkinci satır, w genişliğini içerir.

# kısıtlamalar
# 0 < len(S) < 1000
# 0 < w < len(S)
# Çıkış formatı
# Metinle sarılmış paragrafı yazdırın.

import textwrap
def wrap(string, max_width):
    for i in range(0,len(string)+1,max_width):
        result = string[i:i+max_width]
        if len(result) == max_width:
            print(result)
        else:
            return(result)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)