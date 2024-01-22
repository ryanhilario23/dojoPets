class Pet:
    def __init__(self,name, type,tricks,noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = noise
        self.health = 100
        self.energy = 90


    def sleep(self):
        # increase energy by 25
        self.energy+= 25
        print(f'{self.name} is sleeping')
        return self
    
    def eat(self):
        # increase pet energy by 5 and health by 10
        if self.energy < 100:
            print(f'{self.name} is not hungry')
            return self
        else:
            self.energy += 5
            self.health += 10
            print(f'{self.name} ate his food\n {self.energy, self.health}')
            return self
        
    def play(self):
        # increase health by 5
        if self.energy < 5:
            print(f'{self.name} is to tired to play')
            return self
        else:
            self.health += 5
            print(f'{self.name} is happy to be with you.')
            return self
        
    def noise(self):
        # print pets sound
        print(f'{self.name}: {self.sound}')
        return self


Koro = Pet('Koromaru','dog','flip','borf')
Koro.sleep().noise().noise().play()
