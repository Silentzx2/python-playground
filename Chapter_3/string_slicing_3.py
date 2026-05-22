# What is a string?
# A string is a sequence of characters. It can be enclosed in single quotes (' '), 
# double quotes (" "), or triple quotes (''' ''' or """ """).

name = "Alice"
nameshort = name[0:3] 
character1 = name[1] # This is called slicing. It extracts a portion of the string.
print(nameshort)  # Output: Ali
print(character1)  # Output: l


# What is negative slicing?
# Negative slicing allows you to extract characters from the end of the string.
# This is called step slicing. It extracts characters at regular intervals.
name2 = "inosuke"
print(name2[-7:-1])
print(name2[0:6])
