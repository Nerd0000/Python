import turtle
t = turtle.Turtle()

def part1(): 
  for i in range(6):
    t.circle(10,90)
    t.circle(-10,90)

  t.circle(10,90)
  t.circle(-10,180)



def part2(): 
  for i in range(6):
    t.circle(10,90)
    t.circle(-10,90)

  t.circle(10,90)

part1()
part1()
part2()