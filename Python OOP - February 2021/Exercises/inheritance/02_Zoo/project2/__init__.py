from project2.animal import Animal
from project2.lizard import Lizard
from project2.mammal import Mammal
from project2.reptile import Reptile


mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)
