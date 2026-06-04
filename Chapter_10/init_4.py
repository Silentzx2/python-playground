class student:
    fees = 1200
    subject = "AI & ML"

    def __init__(self, name, lang, age): # Init is a dunder method. which is automatically called.
        self.name = name
        self.lang = lang
        self.age = age
        print("I am creating an object")


david = student("david", "python", 27)
print(david.name, david.fees, david.subject, david.lang, david.age)