with open("/home/david/Documents/dev/PYTHON/Chapter_9/Chapter_9_ps/text.txt") as f:
    content1 =f.read()

with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt") as f:
    content2 =f.read()

if(content1 == content2):
    print("Yes the content is present")
else:
    print("NO we can't find the files")