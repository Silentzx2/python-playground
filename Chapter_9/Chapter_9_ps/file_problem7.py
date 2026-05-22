with open("/home/david/Documents/dev/PYTHON/Chapter_9/Chapter_9_ps/log.txt") as log:
    lines = log.readlines()
    lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes boss we find it. Line no: {lineno} ")
        break
    lineno += 1
else:
    print("sorry boss we did't find python")