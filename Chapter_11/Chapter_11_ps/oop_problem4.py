class complex:  # Complex numbers ka class banaya
    def __init__(self, real, imag):  # Constructor jo real aur imag values store karta hai
        self.real = real  # Real part ko store karo
        self.imag = imag  # Imaginary part ko store karo

    def __add__(self, other):  # Addition operation define karo (+) operator ke liye
        return complex(self.real + other.real, self.imag + other.imag)  # Real parts aur Imag parts ko separately add karo
    
    def __mul__(self, other):  # Multiplication operation define karo (*) operator ke liye
        real_part = self.real * other.real - self.imag * other.imag  # (a*c - b*d)
        imag_part = self.real * other.imag + self.imag * other.real  # (a*d + b*c)
        return complex(real_part, imag_part)  # Naya complex number return karo
    
    def __str__(self):  # String representation method
        return f"{self.real} + {self.imag}i"  # Complex number ko string format me display karo
c1 = complex(1, 3)  # Pehla complex number banao (1 + 3i)
c2 = complex(3, 5)  # Doosra complex number banao (3 + 5i)
print(c1 + c2)  # Dono complex numbers ko add karke result print karo
print(c1 * c2)  # Dono complex numbers ko multiply karke result print karo