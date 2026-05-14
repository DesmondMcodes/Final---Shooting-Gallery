from turtle import *
import time

### CLASS and FUNCTION DEFINITIONS ###

class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.hue = color
        self.alive = True
        self.st()
        self.score = 0
        self.bullets = []
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)
    
    def fire(self):
        if len(self.bullets) < 5:
            self.bullets.append(Bullet(self))

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.pu()
        self.setheading(player.heading())
        self.color(player.hue)
        self.goto(player.xcor(), player.ycor())
        self.player = player
        self.st()
        self.setheading(player.heading())

    def move(self):
        self.forward(7)
        if self.xcor() > 100 or self.xcor() < -100:
            self.setheading(-(self.heading()))
        elif self.heading() == 0:
            self.heading(180)
        if self.ycor() > 230 or self.ycor() < -230:
            self.ht()
            self.player.bullets.remove(self)

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('white')
    pen.begin_fill()
    pen.goto(-100,240)
    pen.goto(100,240)
    pen.goto(100,-240)
    pen.goto(-100,-240)
    pen.goto(-100,240)
    pen.end_fill()

class Block(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.ht()
        self.pu()
        self.speed(0)
        self.shape("square")
        self.goto(x,y)
        self.color(color)
        self.st()

def update():
    if p1.alive and p2.alive:
        for bullet in p1.bullets:
            bullet.move()
            for block in blocks:
                if bullet.distance(block) < 20:
                    block.ht()
                    blocks.remove(block)
                    bullet.ht()
                    p1.bullets.remove(bullet)
                    p1.score += 1
                    print(p1.score)
        for bullet in p2.bullets:
            bullet.move()
            for block in blocks:
                if bullet.distance(block) < 20:
                    block.ht()
                    blocks.remove(block)
                    bullet.ht()
                    p2.bullets.remove(bullet)
                    p2.score += 1
                    print(p2.score)
    screen.ontimer(update, 30)


### PROGRAM ###
screen = Screen()
screen.bgcolor("black")
screen.setup(400,800)
playing_area()
screen.listen()
blocks = []
p1 = Player(40,-200, "red", screen, "d", "a", "s")
p2 = Player(-40,-200, "blue", screen, "Right", "Left", "Down")


for y in range(230, 130, -20):
    for x in range(90, -91, -20):
        if len(blocks) % 3 == 0:
            blocks.append(Block(x,y, "lightgray"))
        elif len(blocks) % 3 == 1:
            blocks.append(Block(x,y, "gray"))
        else:
            blocks.append(Block(x, y, "darkgray"))
    
update()

screen.exitonclick()