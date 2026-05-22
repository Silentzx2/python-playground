mylist = [2, 2, 3, 4, 5]
# squarelist = []
# for i in mylist:
#     squarelist.append(i*i)

# this can be done using list comprehension
squarelist = [i*i for i in mylist]
print(squarelist)