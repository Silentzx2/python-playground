name = input("Enter your name: ")
letter = """ Dear <|name|>, 
  You are selected!
     <|date|>"""
print(letter.replace("<|name|>", (f"{name}")).replace("<|date|>", ("07 April")))