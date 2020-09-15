import turtle

t = turtle.Turtle()
t.lt(90)
t.speed(0)
def frac(i):
    if i < 10:
        return
    else:
        t.forward(i)
        t.lt(45)
        frac(3*i/4)
        t.lt(45)
        frac(3*i/4)
        t.rt(135)
        frac(3*i/4)
        t.rt(45)
        frac(3*i/4)
        t.lt(90)
        t.backward(i)
frac(200)