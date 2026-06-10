a = "\nthis is the very long string with emails like john@example.com adfgnd jane@example.com"
FILE = open("/home/david/Documents/dev/python-playground/Chapter_9/read.txt", "a")
data = FILE.write(a)
FILE.close()