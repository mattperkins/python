    # for loop
lemons = ["john", "paul", "george", "ringo"]

for lemon in lemons:
    if lemon == "john":
        print('john')
    elif lemon == "paul":
        print('paul')
        break    
    else:
        print(lemon)



    # while loop
lemon = 10
lime = 15
while lemon < lime:
    if lemon == 10:
        # ignore 10 and continue
        lemon +=1
        continue
    if lemon % 2 == 0:
        print(str(lemon) + " is equal")
    elif lemon % 2 == 1:
        print(str(lemon) + " is odd")
    lemon += 1
print('Done!')

a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
print("Done!")

