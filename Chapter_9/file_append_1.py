a = "\nthis is the very long string with emails like john@example.com and jane@example.com"
FILE = open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt", "a")
data = FILE.write(a)
FILE.close()