import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.width(1)
t.speed(30)
col=('green','purple','blue')
for i in range(400):
    t.pencolor(col[i%3])
    t.forward(i*3)
    t.right(122)