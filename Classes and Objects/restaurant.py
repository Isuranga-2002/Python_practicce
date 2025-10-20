class Restaurant:
    name = ''
    category = ''
    rating = 0.0
    delivery = True

bobs_burgers = Restaurant()
McDonalds = Restaurant()
PizzaHut = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery= False

McDonalds.name = 'McDonalds'
McDonalds.category = 'Bakery'
McDonalds.rating = 8.9
McDonalds.delivery = True

PizzaHut.name = 'Pizza Hut'
PizzaHut.category = 'Bakery'
PizzaHut.rating = 8.7
PizzaHut.delivery = True



print(vars(bobs_burgers))
print(vars(McDonalds))
print(vars(PizzaHut))

