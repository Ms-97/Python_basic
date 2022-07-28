import numpy as np


def changeInt(a):
    a = 3

def changenumpy(a):
    a[0]=3
    
    
b = 1
bb = np.ones((2))

print(b)
print(bb)

changeInt(b) 
changenumpy(bb)  

print(b)
print(bb[0])     