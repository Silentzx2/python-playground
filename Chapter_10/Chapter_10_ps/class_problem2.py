class calculater():
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"square of the number is: {self.n*self.n}")

    def cube(self):
        print(f"cube of the number is: {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"squareroot of the number is: {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello world")
        a = calculater(4)
        a.square()
        a.cube()
        a.hello()
        a.squareroot()