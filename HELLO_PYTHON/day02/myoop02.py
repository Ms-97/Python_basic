class xi:
    def __init__(self):
        self.money = 1000
    
    def steal(self, smoney):
        self.money += smoney
        
class putin:
    def __init__(self):
        self.nuclear = 5000
    def alzheimer(self):
        self.nuclear -= 1

class JungEun:
    def __init__(self):
        self.missile = 10000
    def ssorau(self):
        self.missile -= 100
        
class Sungwoo(xi, putin, JungEun):
    def __init__(self):
        xi.__init__(self)
        putin.__init__(self)
        JungEun.__init__(self)
        
        
s = Sungwoo()
print("xi:",s.money)
print("putin:",s.nuclear)  
print("JungEun:",s.missile)  

s.steal(400)
s.alzheimer()
s.ssorau()

print("xi steal:",s.money)
print("putin alzheimer:",s.nuclear)  
print("JungEun ssorau:",s.missile)  
       