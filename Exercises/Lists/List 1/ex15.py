import turtle 
t = turtle.Turtle() 
t.speed(0) 
def quadrado(): 
    for i in range(3): 
        t.fd(100) 
        t.lt(120) 
for i in range(4): 
    quadrado() 
    t.lt(90) 
t.ht() 
