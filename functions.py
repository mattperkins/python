    # functions
def lemon(a = "default",b = "default"):
    print('{},{}'.format(a,b))
lemon("Hello")
lemon(a="Unique", b="Value Added")

def radius(radius):
    return 3.142 * radius * radius
def volume(radius, length):
    print("The total is:", int(radius(15)*length))

length = 20
volume(radius,length)
