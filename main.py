from turtle import *
import time

### CLASS and FUNCTION DEFINITIONS ###

class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key, alive):
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
        self.alive = alive
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)
    
    def fire(self):
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

    def move(self):
        self.forward(7)
        if self.xcor() > 230 or self.xcor() < -230:
            self.ht()
            self.player.bullets.remove(self)
        if self.ycor() > 230 or self.ycor() < -230:
            self.ht()
            self.player.bullets.remove(self)

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('white')
    pen.begin_fill()
    pen.goto(-200,240)
    pen.goto(200,240)
    pen.goto(200,-240)
    pen.goto(-200,-240)
    pen.goto(-200,240)
    pen.end_fill()
the world is about as large as earth is the earth is with the circumfrence with the earth's circumfrence ' being about as big as the earth;s circumfre
class Block(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
    def grid(self):
        for y in range(200, 140, -20):
            for x in range(-40, 41, 20):
                if len(blocks) % 3 == 0:
                    blocks.append(Block(x,y, "lightgray"))
                elif len(blocks) % 3 == 1:
                    blocks.append(Block(x,y, "gray"))
                else:
                    blocks.append(Block(x, y, "darkgray"))

### PROGRAM ###
screen = Screen()
screen.bgcolor("black")
screen.setup(80,400)
playing_area()
screen.listen()
blocks = []
p1 = Player(40,-200, "red", screen, "a", "d", "s", True)
p2 = Player(-40,-200, "blue", screen, "Left", "Right", "Down", True)


    


screen.exitonclick()