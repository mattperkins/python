def contacts(dict):
    for key,val in dict.items():
        # print(f"My name is {key} and I live in {val}")
        print("My name is {} and I live in {}".format(key, val))

hometowns = {}

while True:
    name = input('Enter a name:')
    city = input('Enter a city:')
    hometowns[name] = city

    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

contacts(hometowns)