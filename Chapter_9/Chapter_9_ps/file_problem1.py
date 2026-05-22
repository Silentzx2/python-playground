with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt") as FILE:
    data = FILE.read()
    if ("Kansas City" in data):
        print("Kansas City is in the file" )
    else:
        print("Kansas City is not in the file")
