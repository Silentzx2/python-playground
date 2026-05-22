# Defination of function
name = "david"
print(len(name))
print(name.endswith("vid"))
print(name.startswith("dav"))
print(name.capitalize())

# Most Used Python String Functions
s = "hello world"

a = "hello"
len(s)              # length of string

# Case conversion
s.lower()           # lowercase
s.upper()           # uppercase
s.title()           # title case
s.capitalize()      # first letter capital

# Searching
s.find("a")         # returns index or -1
s.index("a")        # returns index or error
s.count("a")        # count occurrences

# Replace & Trim
s.replace("a","b")  # replace text
s.strip()           # remove spaces both sides
s.lstrip()          # left trim
s.rstrip()          # right trim

# Split & Join
s.split()           # string to list
" ".join(list)      # list to string

# Checking
s.isalpha()         # only letters
s.isdigit()         # only numbers
s.isalnum()         # letters + numbers
s.startswith("h")   # starts with
s.endswith("y")     # ends with

# Formatting
s.format()          # old formatting
f"{name}"           # modern f-string