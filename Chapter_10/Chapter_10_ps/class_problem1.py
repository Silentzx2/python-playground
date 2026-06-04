class programmer:
    company = "MICROSOFT"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

e = programmer("david", 12000, 5464)
print(e.name, e.company, e.salary, e.pin)
