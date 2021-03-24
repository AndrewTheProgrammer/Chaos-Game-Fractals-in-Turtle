def barnsley_fern(color='green',pointsRequested=10000):
    #import turtle functions
    from turtle import penup,goto,dot,ht,speed,setworldcoordinates
    #zoom in
    setworldcoordinates(-5,-1,5,15)
    #speed up
    speed(0)
    #hide turtle for better fern visibility
    ht()
    #pen up to prevent lines drawing
    penup()
    #delete the above functions, as I won't need to call them again
    del penup,ht,speed,setworldcoordinates
    #define variables
    global x1,y1
    x1=y1=0
    #create function for simplicity and compaction
        #formuladot()takes the transformation constant and puts a dot where the formula indicates
    def formuladot(a,b,c,d,f):
        global x1,y1
        x2,y2=a*x1+b*y1,c*x1+d*y1+f
        x1,y1=x2,y2
        goto(x1,y1)
        dot('green')
    #import random selection
    from random import randint
    #repeat the following pointsRequested times:
    loopcount=0
    while loopcount<pointsRequested:
        random_act=randint(1,100)
        #if the 1st action is chosen
        if random_act==1: formuladot(0,0,0,0.16,0)
        #if the 2nd action is chosen
        elif 2<=random_act<=86: formuladot(0.85,0.04,-0.04,0.85,1.6)
        #if the 3rd action is chosen
        elif 87<=random_act<=93: formuladot(0.2,-0.26,0.23,0.22,1.6)
        #if the 4th action is chosen
        else: formuladot(-0.15,0.28,0.26,0.24,0.44)
        loopcount+=1
    del x1,y1
