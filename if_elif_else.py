    # if statements
a, b = 0, 1
if a < b:
    print("a ({}) is less than b ({})".format(a,b))
else:
    print("nope!")
print("foo" if a < b else "bar")


    # if statements inside function
def lemon():
    a = 25
    if a < 10:
        print('The number is ({})'.format("less than 10"))
    elif a < 30:
        print('The number is ({})'.format("more than 10, less than 30"))
    else:
        print('The number is above 30')
lemon()

