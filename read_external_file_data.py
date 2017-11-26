    # read external file data
read_file = open('lines.txt')

for line in read_file:
    print(line)


for line in read_file:
    print(line.rstrip())


for line in read_file.readlines():
    print(line, end="")


    # return cursor to start (.seek(0))
read_file.seek(0)
lines = read_file.readlines()
print(lines)


    # read from character 50 to character 100
read_file.seek(50)
read_from_to = read_file.read(100)
print(read_from_to)


# required for improved performance
read_file.close()