# Python 3.10+ mein `match` ... `case` ek pattern matching statement hai.
# Ye switch/case jaise kaam karta hai, lekin zyada powerful hai.
# Example:
# match value:
#     case 1:
#         # agar value 1 hai
#     case "hello":
#         # agar value string "hello" hai
#     case _:
#         # default case

# Simple definition:
# `match` ek expression ko check karta hai aur uski value ke
# against alag-alag `case` patterns ko compare karta hai.
# `case _:` wildcard pattern hai jo sabhi values ko match karta hai.

value = 2
match value:
    case 1:
        print("Value ek hai")
    case 2:
        print("Value do hai")
    case _:
        print("Koi aur value hai")
 