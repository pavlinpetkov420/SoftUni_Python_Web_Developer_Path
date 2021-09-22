from problem_solving_2.pizza_calories.dough import Dough
from problem_solving_2.pizza_calories.topping import Topping
from problem_solving_2.pizza_calories.pizza import Pizza

d = Dough('Milky_Dough', 'Grill_baked', 0.800)
t1 = Topping('Ham', 0.100)
t2 = Topping('Tomatoes', 0.070)
t3 = Topping('Pineapple', 0.095)
t4 = Topping('Olives', 0.100)
t5 = Topping('Waguy', 0.900)
t6 = Topping('Hot Dog', 0.555)

pizza = Pizza('Some_Random_Fun', d, 5)
pizza.add_topping(t5)
pizza.add_topping(t3)
pizza.add_topping(t4)
pizza.add_topping(t6)
# print(pizza.add_topping(t2))
# print(pizza.add_topping(t1)) w

print(pizza.calculate_total_weight())
