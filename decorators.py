def salt(func):
    def pepper(): 
        print('Before')
        func()
        print('After')
    return pepper

@salt
def chips():
    print('Using a Decorator function')
chips()
@salt
def homous():
    print('Using a Decorator function')
homous()

        # as above with comments
# def cheeky(func):
#     # wrapper function (lemon)
#     def lemon():
#         # code before function
#         print('oooh!')
#         func()
#         # code after
#         print('aahhh!')

#     return lemon

# @cheeky
# def question():
#     print('can you reduce the price?')
# question()

# @cheeky
# def answer():
#     print('sure I can')
# answer()

