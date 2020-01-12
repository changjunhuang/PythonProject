import turtle
def drawsnake(rad,angle,len,neckrad):
    a = ['blue','red','yellow','green','pink']
    for i in range(0,len):
        turtle.pencolor(a[i])
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.pencolor('black')
    turtle.circle(rad,angle/3)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*3/4)
def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawsnake(40,80,5,pythonsize/2)
main()