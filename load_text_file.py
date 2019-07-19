
file_name = 'testo.txt'

# load opening and closing resource by hand
f = open(file_name, 'r')
content = f.read()
f.close()
print(content)

# load all lines in a single string
with open(file_name, 'r') as f:
    content = f.read()
print(content)

# load all lines as a list
content = []
with open(file_name, 'r') as f:
    content = f.readlines()
print(content)

# load file line by line
content = []
with open(file_name, 'r') as f:
    for line in f:
        content.append(line)
print(content)