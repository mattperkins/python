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



#     # functions
# def lemon(a = "default",b = "default"):
#     print('{},{}'.format(a,b))
# lemon("Hello")
# lemon(a="Unique", b="Value Added")

# def radius(radius):
#     return 3.142 * radius * radius
# def volume(radius, length):
#     print("The total is:", int(radius(15)*length))

# length = 20
# volume(radius,length)



#     # global variable scope
# def lime():
#     global lemon
#     lemon = "I am lemon"
#     print('some say',lemon)
# lime()
# print('some say',lemon)




#     # dictionaries
# hometowns = {
#     "fred" : "LA",
#     "sandy" : "Berlin",
#     "bob" : "NYC"
# }
# print(hometowns["sandy"])

# print("fred" in hometowns)
# print("bar" in hometowns)

# lemon = {1:2, 2:1}
# print(lemon.keys())
# print(lemon.values())

# print(hometowns.keys())
#     # can be typecast to a list 
#     # print(list(hometowns.keys()))
# hometowns.values()
# city_list = list(hometowns.values())
# print(city_list)
# print(city_list.count("LA"))

#     # add to dictionary
# hometowns["ty"] = "San Diego"
# print(hometowns)

#     # alternate way to create dictionary
# person = dict(name="lottie", age="24", height="5.3")
# print(person["age"])




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





    # sorting and sets
nums = [1,55,55,99,1,9,7,6,3]
print(sorted(nums))
    # capitals will be sorted first 
names = ["bob", "amy", "Fred", "Lottie"]
print(sorted(names))

    # removes duplicates but doesn't preserve order
print(set(nums))

    # use with multiple methods
lemon = {1:2, 1:3, 2:1, 2:2}
print(lemon.keys())
print(lemon.values())
print(set(lemon.values()))




#     # read external file data
# pullIn = open('lines.txt')
# for line in pullIn.readlines():
#     print(line, end="")
