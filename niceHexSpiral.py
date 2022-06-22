import turtle

t=turtle.Pen()
turtle.bgcolor('green')
sides=6
colors=("red", 'yellow', 'blue', 'black', 'purple', 'orange')
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides + x)
    t.left(90/sides+3)
    t.width(x * sides/200)


