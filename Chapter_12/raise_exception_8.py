# Merging dictionaries with the | operator

dict_a = {'name': 'Alice', 'age': 30, 'city': 'New York'}
dict_b = {'name': 'Bob', 'age': 25, 'city': 'Chicago'}

merge = dict_a | dict_b
print(merge)

# Multiple context managers with statement

with (
    open('file1.txt', 'r') as file1,
    open('file2.txt', 'r') as file2
):
    content1 = file1.read()
    content2 = file2.read()
    print(content1)
    print(content2  
)

