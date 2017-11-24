    # dictionaries
hometowns = {
    "fred" : "LA",
    "sandy" : "Berlin",
    "bob" : "NYC"
}
print(hometowns["sandy"])

print("fred" in hometowns)
print("bar" in hometowns)

lemon = {1:2, 2:1}
print(lemon.keys())
print(lemon.values())

print(hometowns.keys())
    # can be typecast to a list 
    # print(list(hometowns.keys()))
hometowns.values()
city_list = list(hometowns.values())
print(city_list)
print(city_list.count("LA"))

    # add to dictionary
hometowns["ty"] = "San Diego"
print(hometowns)

    # alternate way to create dictionary
person = dict(name="lottie", age="24", height="5.3")
print(person["age"])
