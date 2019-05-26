import turtle

import numpy
#turtle.screensize(800, 600, "green")
turtle.screensize() #返回默认大小(400, 300)
turtle.setup(width=0.5, height=0.75, startx=None, starty=None)

turtle.pensize(3)
turtle.pencolor("red")
turtle.fillcolor("pink")
turtle.speed(9)
turtle.hideturtle()
 
'''
turtle.begin_fill()

for _ in range(2):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
'''

#turtle.goto(30,10)

# ρ=a(1−sinθ) Polar coordinates convert to Cartesian coordinates
turtle.begin_fill()
theta = numpy.linspace(0.5*numpy.pi, 1.5*numpy.pi, 1000)
r = 100*(1- numpy.sin(theta))
x = r*numpy.cos(theta)
y = r*numpy.sin(theta)

for coord in range(1000):
   turtle.goto(x[coord], y[coord])

theta = numpy.linspace(-0.5*numpy.pi, 0.5*numpy.pi, 1000)
r = 100*(1- numpy.sin(theta))
x = r*numpy.cos(theta)
y = r*numpy.sin(theta)

for coord in range(1000):
   turtle.goto(x[coord], y[coord])
turtle.end_fill()
turtle.done()