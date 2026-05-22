def rem(l , word):
    n = []
    for item in l:
        if item != word:
            n.append(item.strip(word))
    return n


l = ["rohan", "amit", "rohan", "sachin", "david",]
print(rem(l, "rohan"))