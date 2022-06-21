class Animal:
    def __init__(self):
        self.age = 1
    def happyBirth(self):
        self.age += 1    
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.money = 10000
          
    def albamon(self):
        self.money += 1        
        

h = Human()
print(h.money)
print(h.age)

h.happyBirth()
h.albamon()
print(h.money)
print(h.age)
 
      