with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt") as f:
    content = f.read()

with open("/home/david/Documents/dev/PYTHON/Chapter_9/rename_by_python.txt", "w") as f:
     f.write(content)