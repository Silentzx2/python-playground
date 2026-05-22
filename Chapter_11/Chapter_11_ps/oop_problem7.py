# Vector class ko define karna
class vector:
    # Constructor - x aur y coordinates initialize karte hain
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)

# Pehla vector banate hain coordinates (2, 3, 4) ke saath
v1 = vector([1, 2, 3])
print(len(v1))