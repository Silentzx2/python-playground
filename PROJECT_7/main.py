import secrets

print("Welcome to Bharat bank")



with open("/home/david/Documents/dev/python-playground/PROJECT_7/DATA_BASE.txt", "r") as DATA:
    DATA_BASE = DATA.read()

while True:
    USER_NAME = input("Enter a Username: ")
    if USER_NAME in DATA_BASE or (USER_NAME == ""):
        print("You can't use this")
    else:
        PASSWORD = (USER_NAME + secrets.token_hex(8))
        print("Account creation is completed")
        print(f"Username: {USER_NAME} \nPassword: {PASSWORD}")
        with open("/home/david/Documents/dev/python-playground/PROJECT_7/DATA_BASE.txt", "a") as DATA:
             DATA.write(f"######## [ {USER_NAME} ] ##########\n Username: {USER_NAME} \n Password: {PASSWORD}\n######################\n")
        break