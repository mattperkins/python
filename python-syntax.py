#     # if statements
# a, b = 0, 1
# if a < b:
#     print("a ({}) is less than b ({})".format(a,b))
# else:
#     print("nope!")
# print("foo" if a < b else "bar")


#     # if statements inside function
# def lemon():
#     a = 25
#     if a < 10:
#         print('The number is ({})'.format("less than 10"))
#     elif a < 30:
#         print('The number is ({})'.format("more than 10, less than 30"))
#     else:
#         print('The number is above 30')
# lemon()


    # functions
def lemon(a,b):
    print('{},{}'.format(a,b))
lemon("Hello", "World!")



#     # format string
# lemon = 1.23456
# lime = 9.8765
# print("{1:.2f} {0:.1f}".format(lemon, lime))
# print(f'add {lemon} and {lime}')





#     # for loop
# lemons = ["john", "paul", "george", "ringo"]

# for lemon in lemons:
#     if lemon == "john":
#         print('john')
#     elif lemon == "paul":
#         print('paul')
#         break    
#     else:
#         print(lemon)




    # range 
# // between 1 and 10 in steps of 3
# for n in range(1,10,3):
#     print(n)

# lemon = ["J", "P", "G", "R"]
# for n in range(len(lemon) - 1, -1, -1): # -1 reverses
#     print(n, lemon[n])




#     # while loop
# lemon = 10
# lime = 15
# while lemon < lime:
#     if lemon == 10:
#         # ignore 10 and continue
#         lemon +=1
#         continue
#     if lemon % 2 == 0:
#         print(str(lemon) + " is equal")
#     elif lemon % 2 == 1:
#         print(str(lemon) + " is odd")
#     lemon += 1
# print('Done!')

# a, b = 0, 1
# while b < 50:
#     print(b)
#     a, b = b, a + b
# print("Done!")




#     # read external file data
# pullIn = open('lines.txt')
# for line in pullIn.readlines():
#     print(line, end="")
