from DogClass import *
from VeterinariansClass import *

Dog1 = Dog("Lolly", "Holly", 12)
Dog2 = Dog("Fred", "Ted", 2)
Dog3 = Dog ("Pam", "Sam", 1)
Dog4 = Dog ("Callie", "Sally", 10)
Dog5 = Dog("Rim", "Babar", 4)

Vet1 = Vets("Ibs", 999, "gmail.com", "London", "Dogs")

print(Vet1.patient(), Dog1.name)