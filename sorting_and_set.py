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
