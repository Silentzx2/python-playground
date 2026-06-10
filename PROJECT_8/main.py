import os 
path = input("Enter the path: ")

total = 0
py_files = 0
txt_files = 0

for root, dirs, files in os.walk(path):
    for file in files:
        # finds total flies
        full_path = os.path.join(root, file)
        total += 1
        with open("log.txt", "a") as f:
            f.write(f"[Total] {full_path}\n")
        # finds txt files
        if file.endswith("txt"):
            full_path = os.path.join(root, file)
            print(f"[TXT] {full_path}")
            txt_files += 1
            with open("log.txt", "a") as f:
                f.write(f"[TXT] {full_path}\n")
            # finds py files
        elif file.endswith("py"):
            full_path = os.path.join(root, file)
            print(f"[PY] {full_path}\n")
            py_files += 1
            with open("log.txt", "a") as f:
                f.write(f"[PY] {full_path}\n")
print("\n===== SUMMARY =====")

# Total python files
print("Python files :", py_files)

# Total txt files
print("Text files   :", txt_files)

# Dono ka total
print("Total files  :", total)

with open("log.txt", "a") as f:
    f.write("\n===== SUMMARY =====\n")
    f.write(f"Python file: {py_files}\n")
    f.write(f"Text files: {txt_files}\n")
    f.write(f"Total files: {total}\n")

