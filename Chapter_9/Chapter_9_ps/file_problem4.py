word = "donkey"

with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt", "r") as file:
    content = file.read()
    content_new = content.replace("donkey", "####")

with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt", "w") as file:
    file.write(content_new)

print("Mission succesful boss all sensitive content are removed")