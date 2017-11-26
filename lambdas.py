nums = [1,2,3,4,5,6]

# lambda method
print(list(map(lambda n: n * n,nums)))


# function method
def square(n):
    return n*n

print(list(map(square,nums)))



