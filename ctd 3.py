import turtle
import random
turtle.title("nouran ctd3")  
t = turtle.Turtle()
t.pensize(3)
t.speed(9)
s=1
y=1
for i in range(1,50):
    x=random.choice( ['dark cyan', 'dark red', 'deep pink','dark magenta', 'medium blue', 'pale violet red','rosy brown', 'goldenrod', 'forest green','medium purple'] )
    t.pencolor(x)
    t.right(90)
    t.forward(2+s)
    t.circle(y)
    s+=5
    y+=2
