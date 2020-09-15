import turtle  #importa a bliblioteca turtle, usada para fazer os desenhos

t = turtle.Turtle()

def square(x):  #define a função square
    t.color(x,x)
    t.begin_fill()
    for i in range(4):
        t.forward(180)
        t.left(90)
    t.end_fill()
    
def move(x,y): #move o ponteiro para a coordenada sem desenhar
    t.up()
    t.goto(x,y)
    t.down()

move(-190,-190)   
square('blue') #primeiro quadrado

move(10,-190)  #segundo
square('yellow') 

move(10,10)  #terceiro
square('green') 

move(-190, 10)  #quarto
square('red') 
