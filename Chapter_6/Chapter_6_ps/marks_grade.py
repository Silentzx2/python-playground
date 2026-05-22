marks1 = int(input("Enter the math marks: "))
marks2 = int(input("Enter the physics marks: "))
marks3 = int(input("Enter the chemistry marks: "))

# Check for total percentage

total_percentage = (100)*(marks1 + marks2 + marks3) / 300
print("Your total percentage is:", total_percentage, "%")
if (total_percentage >= 40):
    print("You have passed the exam.")
else:
    print("You have failed the exam.")