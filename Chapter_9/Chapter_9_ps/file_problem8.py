with open("/home/david/Documents/dev/PYTHON/Chapter_9/Chapter_9_ps/text.txt") as f:
    content =f.read()

with open("copy.txt", "w") as f:
     f.write(content)