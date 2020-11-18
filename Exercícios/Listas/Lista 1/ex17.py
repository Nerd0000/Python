import turtle 
t = turtle.Turtle() 
t.speed(0) 
def triangulo(): 
    for i in range(4): 
        t.fd(100) 
        t.lt(90) 
for i in range(4): 
    triangulo() 
    t.lt(90) 
t.ht() 
