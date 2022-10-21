# Task
# Kevin and Stuart want to play the ‘The Minion Game’.

# Game Rules

# Both players are given the same string, S.

# Both players have to make substrings using the letters of the string S.

# Stuart has to make words starting with consonants.

# Kevin has to make words starting with vowels.

# The game ends when both players have made all possible substrings.


# Scoring

# A player gets +1 point for each occurrence of the substring in the string S.

# Your task is to determine the winner of the game and their score.

# Input Format
# A single line of input containing the string S.

# Note: The string S will contain only uppercase letters: [A – Z].


# Constraints
# 0 <= len(S) <= 10^6

# Output Format
# Print one line: the name of the winner and their score separated by a space.
# If the game is a draw, print Draw.

#-------------------------------------------------

# Görev
# Kevin ve Stuart 'Minyon Oyunu' oynamak istiyorlar.

# Oyun kuralları

# Her iki oyuncuya da aynı dizi verilir, S.

# Her iki oyuncu da S dizisinin harflerini kullanarak alt diziler oluşturmalıdır.

# Stuart ünsüzlerle başlayan kelimeler yapmak zorunda.

# Kevin sesli harflerle başlayan kelimeler yapmak zorunda.

# Oyun, her iki oyuncu da tüm olası alt dizileri yaptığında sona erer.


# Puanlama

# Bir oyuncu, S dizisindeki alt dizinin her oluşumu için +1 puan alır.

# Göreviniz oyunun kazananını ve puanını belirlemek.

# Giriş Formatı
# S dizesini içeren tek bir girdi satırı.

# Not: S dizisi yalnızca büyük harfleri içerecektir: [A – Z].


# Kısıtlamalar
# 0 <= len(S) <= 10^6

# Çıkış formatı
# Bir satır yazdırın: kazananın adı ve bir boşlukla ayrılmış puanı.
# Oyun berabere ise, Draw yazdırın.

def minion_game(string):
    # your code goes here
    vowel = 'aeiou'.upper()
    strl = len(string)
    kevin = sum(strl-i for i in range(strl) if string[i] in vowel)
    stuart = strl*(strl + 1)/2 - kevin

    if kevin == stuart:
        print ('Draw')
    elif kevin > stuart:
        print ('Kevin %d' % kevin)
    else:
        print ('Stuart %d' % stuart)
if __name__ == '__main__':
    s = input()
    minion_game(s)