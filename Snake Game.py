import turtle
import random
import time
delay = 0.1
score = 0
highestscore = 0
#snake_bodies:-
bodies = []
#making a screen:-
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("white")
s.setup(width = 700,height = 700)
#making snake head:-
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.fillcolor("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"
#Snake Food:-
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.fillcolor("orange")
food.penup()
food.ht()
food.goto(0,250)
food.st()
#score board:-
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-300,-300)
sb.write("score: 0  |  highest: 0")

def moveup():
    if head.direction!="down":
        head.direction ="up"
def movedown():
    if head.direction!="up":
        head.direction ="down"
def moveleft():
    if head.direction!="right":
        head.direction ="left"
def moveright():
    if head.direction!="left":
        head.direction ="right"
def movestop():
    head.direction="stop"
def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20)
#Event Handling - key Mappings
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveright,"Right")
s.onkey(moveleft,"Left")
s.onkey(movestop,"space")
#Main Loop:-
while True:
    #This is to update the screen:-
    s.update()
    #check the collision with border:-
    if head.xcor()>340:
        head.setx(-340)
    if head.xcor()<-340:
        head.setx(340)
    if head.ycor()>340:
        head.sety(-340)
    if head.ycor()<-340:
        head.sety(340)
    #check the collision with food:-
    if  head.distance(food)<20:
        #move the food to new random place
        x = random.randint(-340,340)
        y = random.randint(-340,340)
        food.goto(x,y)
        #increase the length of the snake :-
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("green")
        body.fillcolor("green")
        bodies.append(body)#append new body
        #increase the score:-
        score+=10
        #change the delay:-
        delay-=0.001
        #update the highest score:-
        if score>highestscore:
            highestscore = score
        sb.clear()
        sb.write("Score: {} Highest Score:{}".format(score,highestscore))
    #move the snake bodies:-
    for index in range(len(bodies)-1,0,-1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x,y)
    move()
    #check collision of snake body with itself:-
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide bodies:-
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1
            #update the scoreboard:-
            sb.clear()
            sb.write("Score: {} | Highest Score: {}".format(score,highestscore))
    time.sleep(delay)
s.mainloop()
