class employee:  # Employee class define kar rahe hain
    salary = 34  # Class variable: base salary 34 set ki
    increment = 20  # Class variable: increment 20% set ki
    @property  # Yeh decorator property banata hai - jisko method ki tarah nahi call karte, attribute ki tarah access karte hain
    def salaryafterincrement(self):  # Method define kiya jo salary+increment calculate karega
        # yeh property method hai jo salary ke baad increment add karke value dega
        return (self.salary) + (self.salary) * ((self.increment/100))  # Salary + (salary ka 20%) return karega = 34 + 6.8 = 40.8
    
    # neeche ka code galat syntax tha, isliye comment kiya hua hai
    # @increment.__setattr__ Python mein valid decorator nahi hai
    # setter banane ke liye @property_name.setter use karte hain, yahan nahi
    # @increment.__setattr__
    # def increment(self, salary):
    #     self.increment = (( salary/self.salary)-1)*100


# Object creation
e = employee()  # Employee class ka instance 'e' banaya
# WRONG: salaryafterincrement is a @property (not a method), so don't call it with ()
# CORRECT: Access it as e.salaryafterincrement (without parentheses)
print(e.salaryafterincrement)  # Property ko access kiya (parentheses ke bina) - output: 40.8 aayega, TypeError nahi