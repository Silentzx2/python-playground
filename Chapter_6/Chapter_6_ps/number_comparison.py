spam_keyword_1 = "viagra"
spam_keyword_2 = "lottery winner"
spam_keyword_3 = "claim prize"
spam_keyword_4 = "act now"

msg = input("Enter your message: ")

if ((spam_keyword_1 in msg) or (spam_keyword_2 in msg) or (spam_keyword_3 in msg) or (spam_keyword_4 in msg)):
    print("This message is a spam.")
else:
    print("This message is not a spam.")