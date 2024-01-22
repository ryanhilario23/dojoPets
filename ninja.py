from Koro import*
class Ninja:
    def __init__(self,first_name, last_name, treats, pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        print(f'{self.first_name} went for a walk {self.pet.name}')
        self.pet.play()
        return self

    def feed(self):
        print(f'{self.first_name} gave {self.pet.name} his food.\n{self.pet.name}\'s bowl: {self.pet_food}')
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        print(f'{self.pet.name} does not like this')
        return self
        


treats =  'bacon'
pet_food = 'Raw meat'

Jake = Ninja('Jake','Agbuya',treats, pet_food, Koro)
print('----------')
Jake.feed().bathe().walk()