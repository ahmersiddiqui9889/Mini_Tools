'''
Snake Game
Author - 
- set sound=True for sound
'''

# by peppergreen00

'''
Author_Notes
for sound :-
- set sound=True
- uncomment the import playsound
- replace the location given below with the absolute position of the sound files
'''

import turtle
from random import randrange,choice
import time
# from playsound import playsound

sound = False

turtle.tracer(0)
# Score
score = 0
highscore = 0
delay = 0.2

# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("snake")
wn.setup(450,450)

# Pen
pen = turtle.Turtle()
pen.ht()
pen.pensize(3)
pen.color("white")
pen.pu()
pen.goto(-230,230)
pen.pd()
for i in range(4):
    pen.fd(460)
    pen.rt(90)
    
pen2 = turtle.Turtle()
pen2.ht()
pen2.color("white")
pen2.pu()

# Snake Head
headdirection = "up"
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()

# Food
food = turtle.Turtle()
color = choice(['red','blue','green','yellow','orange'])
food.shape('circle')
food.shapesize(0.8)
food.pu()
food.color(color)
x=randrange(-220,220,20)
y=randrange(-220,220,20)
food.goto(x,y)

# Actions
def up():
    global headdirection
    if headdirection != "down":
        headdirection = "up"

def down():
    global headdirection
    if headdirection != "up":
        headdirection = "down"

def left():
    global headdirection
    if headdirection != "right":
        headdirection = "left"

def right():
    global headdirection
    if headdirection != "left":
        headdirection = "right"

def move():
    global headdirection, head
    if headdirection == "up":
        head.sety(head.ycor()+20)
    if headdirection == "down":
        y = head.ycor()
        head.sety(head.ycor()-20)
    if headdirection == "left":
        x = head.xcor()
        head.setx(head.xcor()-20)
    if headdirection == "right":
        x = head.xcor()
        head.setx(head.xcor()+20)




wn.listen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")





# Main Program
firstfood = False
segments = []
while True:

    turtle.update()
    

    # Border Check
    if head.xcor() > 230 or head.xcor() < -230 or head.ycor() > 230 or head.ycor() < -230:
        if sound == True:
            playsound("C:\\Users\\91870\\Desktop\\python games\\snake\\gameover.wav",False)
        time.sleep(1)
        head.home()
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        firstfood = False
        delay = 0.2
        score = 0
    
    # Food Eat
    if head.distance(food) < 10:
        if sound == True:
            playsound("C:\\Users\\91870\\Desktop\\python games\\snake\\eat2.wav",False)
        x = randrange(-220,220,20)
        y = randrange(-220,220,20)
        s=turtle.Turtle()
        color = choice(['red','blue','green','yellow','magenta','cyan','purple'])
        s.color("orange")
        s.shape('square')
        food.goto(x,y)
        food.shape('circle')
        food.shapesize(0.8)
        food.color(color)

        s.pu()
        segments.append(s)
        firstfood = True
        score += 10
        if score > highscore:
            highscore = score
        delay -= 0.001
        



    # Collision with body
    for segment in segments:
        if head.distance(segment) < 10:
            if sound == True:
                playsound("C:\\Users\\91870\\Desktop\\python games\\snake\\gameover.wav",False)
            time.sleep(2)
            head.home()
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            firstfood = False
            delay = 0.2
            score = 0

    # Printing Score
    pen2.clear()
    pen2.goto(400,200)
    pen2.write("Highscore: {}".format(highscore),align="left",font=("Courier",24))
    pen2.goto(400,150)
    pen2.write("Score: {}".format(score),align="left",font=("Courier",24))
    
    time.sleep(delay)

    # Segment Alignment
    if firstfood == True:

        for segm in range(len(segments)-1,0,-1):
            x=segments[segm-1].xcor()
            y=segments[segm-1].ycor()
            segments[segm].goto(x,y)
            
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
        
    # Moving Head
    move()
