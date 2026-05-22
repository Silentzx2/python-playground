with open("/home/david/Documents/dev/PYTHON/Chapter_9/Chapter_9_ps/log.txt") as log:
    content = log.read()

if("python" in content):
    print("yes boss we find it ")
else:
    print("sorry boss we did't find python")