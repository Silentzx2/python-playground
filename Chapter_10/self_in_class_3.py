class student:
    fees = 1200
    subject = "AI & ML"
    def getinfo(self):
        print(f"The subject is: {self.subject}")
    @staticmethod
    def greet():
        print("Hey good morning, boss")

david = student()
david.name = "david"  # type: ignore
print(david.name, david.fees, david.subject) # type: ignore
david.getinfo()
david.greet()
