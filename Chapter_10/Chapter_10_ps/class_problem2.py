class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of a number is {self.num*self.num}")

    def cube(self):
        print(f"The cube of a number is {self.num*self.num*self.num}")

    def squareroot(self):
        print(f"The squareroot of a number is {self.num**1/2}")

c = calculator(4)
c.square()
c.cube()
c.squareroot()
    