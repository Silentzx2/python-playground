
# FILE = open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt")
# data = FILE.read()
# print(data)
# FILE.close()

# this can be written as
with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt") as FILE:
    data = FILE.read()
    print(data)