def sierpinski(backgcolor='white',color1='black',color2='black',color3='black',vertex1x=0,vertex1y=200,vertex2x=300,vertex2y=-200,vertex3x=-300,vertex3y=-200,pointX=0,pointY=0,pointsRequested=10000):
    from turtle import penup,goto,dot,speed,hideturtle,bgcolor
    hideturtle()
    penup()
    speed(0)
    bgcolor(backgcolor)
    del speed,hideturtle,penup,bgcolor
    def putdot(color,xcor,ycor):
        goto(xcor,ycor)
        dot(color)
    putdot(color1,pointX,pointY)
    putdot(color1,vertex1x,vertex1y)
    putdot(color2,vertex2x,vertex2y)
    putdot(color3,vertex3x,vertex3y)
    from random import randint
    loopcount=0
    while loopcount<pointsRequested:
        random_vertex=randint(1,3)
        if random_vertex==1:
            pointX,pointY=(pointX+vertex1x)/2,(pointY+vertex1y)/2
            putdot(color1,pointX,pointY)
        elif random_vertex==2:
            pointX,pointY=(pointX+vertex2x)/2,(pointY+vertex2y)/2
            putdot(color2,pointX,pointY)
        else:
            pointX,pointY=(pointX+vertex3x)/2,(pointY+vertex3y)/2
            putdot(color3,pointX,pointY)
        loopcount+=1
def sierpinskitypetwo(backgcolor='white',color1='black',color2='black',color3='black',vertex1x=0,vertex1y=200,vertex2x=300,vertex2y=-200,vertex3x=-300,vertex3y=-200,pointX=0,pointY=0,pointsRequested=10000):
    from turtle import penup,goto,dot,speed,hideturtle,bgcolor,pencolor
    hideturtle()
    penup()
    speed(0)
    bgcolor(backgcolor)
    del speed,hideturtle,penup,bgcolor,backgcolor
    def putdot(xcor,ycor):
        goto(xcor,ycor)
        dot()
    pencolor(color1)
    putdot(vertex1x,vertex1y)
    pencolor(color2)
    putdot(vertex2x,vertex2y)
    pencolor(color3)
    putdot(vertex3x,vertex3y)    
    from random import randint
    loopcount=0
    while loopcount<pointsRequested:
        random_vertex=randint(1,3)
        if random_vertex==1:
            pointX,pointY=(pointX+vertex1x)/2,(pointY+vertex1y)/2
            putdot(pointX,pointY)
            pencolor(color1)
        elif random_vertex==2:
            pointX,pointY=(pointX+vertex2x)/2,(pointY+vertex2y)/2
            putdot(pointX,pointY)
            pencolor(color2)
        else:
            pointX,pointY=(pointX+vertex3x)/2,(pointY+vertex3y)/2
            putdot(pointX,pointY)
            pencolor(color3)
        loopcount+=1
