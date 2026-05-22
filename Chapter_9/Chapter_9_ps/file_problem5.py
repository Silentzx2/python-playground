word = ["donkey", "bad", "ganda", "noob"]

with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt", "r") as file:
    content = file.read()

    for words in word:
        content = content.replace(words , "#" * len(word))

    with open("/home/david/Documents/dev/PYTHON/Chapter_9/read.txt", "w") as file:
        file.write(content)

print("Mission succesful boss all sensitive content are removed")