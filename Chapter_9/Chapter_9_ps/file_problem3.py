def table(n):    
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {i*n}\n"

    with open(f"/home/david/Documents/dev/PYTHON/table/table_{n}.txt", "w") as FILE:
        FILE.write(table)



for i in range(2, 21):
    table(i)
