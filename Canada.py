import turtle
import time

#setup
t = turtle.Turtle()
t.ht()
t.lt(90)
t.speed(0)


def move(x,y): #move o ponteiro para a coordenada sem desenhar
    t.up()
    t.goto(x,y)
    t.down()

def tree(i): # codigo para desenhar a folha
    if i < 1:
        return
    else:
        t.begin_fill
        t.forward(i)
        t.lt(45)
        tree(i/2)
        t.rt(90)
        tree(i/2)
        t.lt(45)
        t.fd(i)
        tree(i/2)
        t.bk(i)
        t.bk(i)
        t.end_fill

#capa 1
t.color('blue')
t.write("Canada Fractal", align = 'center', font= ('OldManBookStyle', 40, 'bold'))
time.sleep(5)
t.clear()# limpa

# cria a folha
move(0, -20)
t.color('red')  
t.pensize(3)
tree(50)

# retangulos e linha
move(250, 220)

t.begin_fill() #fill

t.rt(180)
t.fd(270)

t.rt(90)
t.fd(100)

t.fd(400) #linha
t.bk(400) #linha

t.rt(90)
t.fd(270)

t.rt(90)
t.fd(100)

t.lt(180) #linha
t.fd(500) #linha

t.lt(90)
t.fd(270)

t.lt(90)
t.fd(100)

t.lt(90)
t.fd(270)

# finalização do desenho
t.end_fill() # fill
time.sleep(5) # espera
t.clear()

move(0,0)

# agradecimento
t.write("Obrigado por assisitir!", align = 'center', font= ('OldManBookStyle', 40, 'bold'))
time.sleep(5)
