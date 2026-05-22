class programmer:
    company = "Microsoft"
    def __init__(self, name , salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("david", 1299990, 718234)
print(p.name, p.salary, p.pin)