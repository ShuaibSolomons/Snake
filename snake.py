import turtle
import random
import time

rng = random.Random()
wn = turtle.Screen()
hollie = turtle.Turtle()
hollie.speed(0)
hollie.penup()
target = turtle.Turtle()
target.penup()
wn.delay()
wn.tracer(1,10)


b = 1
stamps = []


rectangle = ((-5,-5),(-5,5),(5,5),(5,-5))
myshape = turtle.Shape("compound")
myshape.addcomponent(rectangle,"black","green")
wn.register_shape("rectangle",myshape)
hollie.shape("rectangle")


square = ((-5,-5),(-5,5),(5,5),(5,-5))
myshape = turtle.Shape("compound")
myshape.addcomponent(square,"red")
wn.register_shape("square",myshape)
target.shape("square")

def gener():
    x = rng.randrange(-200,200)
    y = rng.randrange(-200,200)
    target.goto(x,y)

def up():
    if hollie.heading() == 0 or hollie.heading() == 180: hollie.setheading(90)
def down():
    if hollie.heading() == 0 or hollie.heading() == 180: hollie.setheading(270)
def right():
    if hollie.heading() == 90 or hollie.heading() == 270: hollie.setheading(0)
def left():
    if hollie.heading() == 90 or hollie.heading() == 270: hollie.setheading(180)
def teleport():
    hollie.forward(100)

    
def start_snake(x,y):
    target.goto(x,y)
    starter = 0
    counter = 0
    score = 0
    a = time.clock()
    while True:
        wn.title("You have eaten {}, of 6 eatables".format(counter))
        stamps.append(hollie.stamp())
        hollie.clearstamp(stamps[0])
        x = hollie.xcor()
        y = hollie.ycor()
        x2 = target.xcor()
        y2 = target.ycor()
        if x>=x2-5 and x<=x2+5 and y>=y2-5 and y<=y2+5:
            gener()
            counter+=1
            if counter ==6:
                b = time.clock()
                target.ht()
                target.write("You have finished the game in {}".format(b))
                break
            else: continue
            score+=10

        elif starter >= 10:
            del stamps[0]
        
        print (stamps)
        starter += 1
        hollie.forward(5)
        wn.onkey(up,"Up")
        wn.onkey(down,"Down")
        wn.onkey(right,"Right")
        wn.onkey(left,"Left")
        wn.onkey(teleport,"space")
        wn.listen()

wn.onclick(start_snake)
wn.listen()
wn.mainloop()
