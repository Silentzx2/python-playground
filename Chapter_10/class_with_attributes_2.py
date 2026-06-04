class student:
    fees = 1200
    subject = "AI & ML"

david = student()
david.name = "david"  # type: ignore
print(david.name, david.fees, david.subject) # type: ignore

rohan = student()
rohan.name = "rohan"  # type: ignore
print(rohan.name, rohan.fees, rohan.subject) # type: ignore