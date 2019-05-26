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

pointNum = 300
 
# ρ=a(1−sinθ) Polar coordinates convert to Cartesian coordinates
def drawplot():
   turtle.begin_fill()
   theta = numpy.linspace(0.5*numpy.pi, 2.5*numpy.pi, pointNum)
   r = 100*(1- numpy.sin(theta))
   x = r*numpy.cos(theta)
   y = r*numpy.sin(theta)

   for coord in range(pointNum):
      turtle.goto(x[coord], y[coord])

   turtle.end_fill()

def drawplot2():
   turtle.begin_fill()
   theta = numpy.linspace(0.5*numpy.pi, 2.5*numpy.pi, pointNum)
   r2 = 50 * numpy.sqrt(225 / (17 - 16 * numpy.sin(theta) * numpy.sqrt(numpy.cos(theta) * numpy.cos(theta))))
   x = r2*numpy.cos(theta)
   y = r2*numpy.sin(theta)

   turtle.penup()
   turtle.goto(x[0], y[0])
   turtle.pendown()
   for coord in range(0, pointNum):
      turtle.goto(x[coord], y[coord])

   turtle.end_fill()

if __name__ == "__main__":
   try:
      #drawplot()
      drawplot2()
      turtle.done() 
   except:
      exit()


