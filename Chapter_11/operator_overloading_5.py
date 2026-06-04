class add:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n


n = add(435)
m = add(3)
print(n + m)