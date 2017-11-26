# how to use this file:
# $ python3
# $ from barTab_exercise import Tab
# $ table1 = Tab()
# // now create order \\
# $ table1.add('wine')
# $ table1.add('veggie')
# $ table1.add('desert')
# // print bill including tax and service \\
# $ table1.print_bill(10,10)
# ------------------------------------------

class Tab:
    menu = {
        'wine': 5,
        'beer': 5,
        'soft_drink': 5,
        'chicken': 5,
        'beef': 5,
        'veggie': 5,
        'desert': 5,
    }

    def __init__(self):
        self.total = 0
        self.items = []
    def add(self,item):
        self.items.append(item)
        self.total += self.menu[item]
    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service
        
        for item in self.items:
            print(f'{item:10} £{self.menu[item]}')
        print(f'{"Total":10} £{total:.2f}')
