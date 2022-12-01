# Task
# For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

# The real and imaginary precision part should be correct up to two decimal places.

# Input Format
# One line of input: The real and imaginary part of a number separated by a space.

# Output Format
# For two complex numbers C and D, the output should be in the following sequence on separate lines:

# C + D
# C – D
# C * D
# C / D
# mod(C)
# mod(D)
# For complex numbers with non-zero real (A) and complex part (B), the output should be in the following format: A+ Bi

# Replace the plus symbol (+) with a minus symbol (-) when B < 0.

# For complex numbers with a zero complex part i.e. real numbers, the output should be: A + 0.00i

# For complex numbers where the real part is zero and the complex part (B) is non-zero, the output should be: B + 0.00i


# Sample Input

# 2 1
# 5 6
# Sample Output

# 7.00+7.00i
# -3.00-5.00i
# 4.00+17.00i
# 0.26-0.11i
# 2.24+0.00i
# 7.81+0.00i
# Concept
# Python is a fully object-oriented language like C++, Java, etc.


# Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.

# __add__-> Can be overloaded for + operation
# __sub__ -> Can be overloaded for - operation
# __mul__ -> Can be overloaded for * operation

#------------------------------------------------------------

# Görev
# Bu meydan okuma için size iki karmaşık sayı verilir ve bunların toplama, çıkarma, çarpma, bölme ve modül işlemlerinin sonucunu yazdırmanız gerekir.

# Gerçek ve sanal kesinlik kısmı iki ondalık basamağa kadar doğru olmalıdır.

# Giriş Formatı
# Bir satır girdi: Bir sayının boşlukla ayrılmış gerçek ve sanal kısmı.

# Çıkış formatı
# İki karmaşık sayı C ve D için çıktı, ayrı satırlarda aşağıdaki sırada olmalıdır:

# C + D
# C – D
# C * D
# C / D
# mod(C)
# mod(D)
# Sıfır olmayan gerçel (A) ve karmaşık kısım (B) içeren karmaşık sayılar için çıktı şu biçimde olmalıdır: A+ Bi

# B < 0 olduğunda artı sembolünü (+) eksi sembolü (-) ile değiştirin.

# Sıfır karmaşık kısmı olan karmaşık sayılar, yani gerçek sayılar için çıktı şöyle olmalıdır: A + 0.00i

# Gerçel kısmı sıfır ve (B) karmaşık kısmının sıfır olmadığı karmaşık sayılar için çıktı şöyle olmalıdır: B + 0.00i


# Örnek Giriş

# 2 1
# 5 6
# Örnek Çıktı

# 7.00+7.00i
# -3.00-5.00i
# 4.00+17.00i
# 0.26-0.11i
# 2.24+0.00i
# 7.81+0.00i
# Konsept
# Python, C++, Java vb. gibi tamamen nesne yönelimli bir dildir.


# Adından önce ve sonra çift alt çizgi bulunan yöntemler, yerleşik yöntemler olarak kabul edilir. Tercümanlar tarafından kullanılırlar ve genellikle aşırı yüklenmiş operatörlerin veya diğer yerleşik işlevlerin uygulanmasında kullanılırlar.

# __add__-> + işlemi için aşırı yüklenebilir
# __sub__ -> - işlemi için aşırı yüklenebilir
# __mul__ -> * işlemi için aşırı yüklenebilir


import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex((self.real+no.real), self.imaginary+no.imaginary)

    def __sub__(self, no):
        return Complex((self.real-no.real), (self.imaginary-no.imaginary))

    def __mul__(self, no):
        r = (self.real*no.real)-(self.imaginary*no.imaginary)
        i = (self.real*no.imaginary+no.real*self.imaginary)
        return Complex(r, i)

    def __truediv__(self, no):
        conjugate = Complex(no.real, (-no.imaginary))
        num = self*conjugate
        denom = no*conjugate
        try:
            return Complex((num.real/denom.real), (num.imaginary/denom.real))
        except Exception as e:
            print(e)

    def mod(self):
        m = math.sqrt(self.real**2+self.imaginary**2)
        return Complex(m, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')