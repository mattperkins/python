        # classes
class Lemon:
    def __init__(self):
     self.name = "Fred"
     self.age = 34
     self.city = "LA"
    
    # instance method
    def business(self):
        return f"{self.name} works in {self.city}"

lime = Lemon()
print(f'{lime.name} is {lime.age}')
print(lime.business())

    # create new 'class' instance (Person)
class Person:
    # class level attribute
    species = 'human'

    # instance attributes
    def __init__(self, name, age, city):
        self.name = name
        self.age = age  
        self.city = city

    # class method
    @classmethod
    def classy(cls):
        return f'on earth there are {cls.species}'
    
    # static method
    @staticmethod
    def walk(pace = 'approx. 1.3mph'):
        return f'walks at {pace}'

    # instance of Person
Sandy = Person('Sandy', 24, 'LA')
print(f'{Sandy.name}')

Bob = Person('Bob', 55, 'NYC')
print(f'{Bob.name} is a {Bob.species} and lives in {Bob.city}') 

Lottie = Person('Lottie', '27', 'London')
print(f'{Lottie.name} knows {Lottie.classy()}')

    # using class method    
print(Person.classy())

    # using static method
print(f'{Lottie.name} {Lottie.walk()}')
print(f'{Bob.name} {Bob.walk("approx 1.5mph")}')