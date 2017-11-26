def sequence_filter(line):
    return "##" not in line

with open('lines.txt') as new_file:
    lines = new_file.readlines()
    print(list(filter(sequence_filter, lines)))

# continue program / doesnt require .close()