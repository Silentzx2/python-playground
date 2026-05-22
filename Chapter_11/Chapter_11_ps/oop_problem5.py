# Vector class ko define karna
class vector:
    # Constructor - x aur y coordinates initialize karte hain
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __add__ method - do vectors ko add karne ke liye
    def __add__(self, other):
        # X coordinates ko add karte hain aur Y coordinates ko add karte hain
        return vector(self.x + other.x, self.y + other.y)

    # __str__ method - vector ko string format mein display karne ke liye
    def __str__(self):
        # Vector ko (x, y) format mein return karte hain
        return f"({self.x}, {self.y})"

# Pehla vector banate hain coordinates (2, 3) ke saath
v1 = vector(2, 3)
# Dusra vector banate hain coordinates (4, 5) ke saath
v2 = vector(4, 5)
# Dono vectors ko add karte hain aur result print karte hain (6, 8)
print(v1 + v2)  # Output: (6, 8)