
    # read external file data
pullIn = open('lines.txt')
for line in pullIn.readlines():
    print(line, end="")
