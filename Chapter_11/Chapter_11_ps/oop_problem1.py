class twodvator:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"vactor is {self.i}i + {self.j}j")



class threedvactor(twodvator):
    def __init__(self, i, j, k):
        self.i = i
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"vactor is {self.i}i + {self.j}j + {self.k}")

a = twodvator(1, 2)
a.show()
b = threedvactor(1,2,3)
b.show()