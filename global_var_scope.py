    # global variable scope
def lime():
    global lemon
    lemon = "I am lemon"
    print('some say',lemon)
lime()
print('some say',lemon)
