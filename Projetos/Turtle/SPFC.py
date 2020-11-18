import turtle

t = turtle.Turtle()

def goto(x,y):
    t.up()
    t.goto(x,y)
    t.down()

def square(l):
    t.begin_fill()
    for i in range(2):
        t.lt(90)
        t.fd(l)
        t.lt(90)
        t.fd(l/3)
    t.end_fill()

# black sqaure
goto(-90, 45)

t.seth(270)
square(180)

# white "SPFC"
goto(0, 45)
t.color('white') ###

t.write('SPFC', align= 'center', font= ('Arial', 40, 'bold'))

# diamond
goto(-100, 35)
t.color('black') ###

t.seth(90)

t.fd(80)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(80) 
print(t.xcor())

t.goto(0, -110)
t.goto(-100, 35)

# triangulo vermelho
t.color('red')
goto(-80, 30)

t.begin_fill()

t.seth(0)
t.fd(70)
t.rt(90)
t.fd(110)
t.goto(-80, 30)

t.end_fill()

# triangulo preto
t.color('black')
goto(80, 30)

t.begin_fill()

t.seth(0)
t.fd(-70)
t.rt(90)
t.fd(110)
t.goto(80, 30)

t.end_fill()