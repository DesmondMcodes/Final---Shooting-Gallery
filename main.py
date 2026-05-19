from turtle import *
import time

start = time.time()
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
            self.setheading(180 - self.heading())
        elif self.ycor() < -230:
            self.die()
            
    def die(self):
        self.ht()
        if self in self.player.bullets:
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
        self.health = 0
        self.colors = ["red", "yellow"]
    def damage(self, players, scores):
        self.health -= 1
        if self.health == -3:
            self.ht()
            blocks.remove(self)
            scores.score += 1

        else:
            self.color(self.colors[self.health])

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.ht()
        self.color("white")
        self.pu()
        self.goto(x, y)
        self.score = 0
        self.write(f"Score: {self.score}", font = ("arial",15, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font = ("arial",15, "normal"))


def create_rows(blocks):
    for x in range(90, -91, -20):
        if len(blocks) % 3 == 0:
            blocks.append(Block(x,230, "lightgray"))
        elif len(blocks) % 3 == 1:
            blocks.append(Block(x,230, "gray"))
        else:
            blocks.append(Block(x, 230, "darkgray"))

def game_over
def update():
    global start
    if time.time() - start > 3:
        start = time.time()
        #move all blocks down create new row
        screen.tracer(0)
        for block in blocks:
            block.goto(block.xcor(), block.ycor() - 20)
            if block.ycor() < -200:
                print("block broken")
                block.ht()
                blocks.remove(block)
        create_rows(blocks)
        screen.tracer(1)
    if p1.alive and p2.alive:
        for bullet in p1.bullets:
            bullet.move()
            for block in blocks:
                if bullet.distance(block) < 20:
                    bullet.die()
                    block.damage(p1, score1)
                    score1.update_score()
        for bullet in p2.bullets:
            bullet.move()
            for block in blocks:
                if bullet.distance(block) < 20:
                    bullet.die()
                    block.damage(p2, score2)
                    score2.update_score()

    screen.ontimer(update, 30)


### PROGRAM ###

screen = Screen()
screen.bgcolor("black")
screen.setup(400,800)
playing_area()
screen.listen()
blocks = []
p1 = Player(40,-200, "red", screen, "Right", "Left", "Down")
p2 = Player(-40,-200, "blue", screen, "d", "a", "s")
score1 = Score(25, 250)
score2 = Score(-90, 250)

screen.tracer(0)
for y in range(230, 130, -20):
    for x in range(90, -91, -20):
        if len(blocks) % 3 == 0:
            blocks.append(Block(x,y, "lightgray"))
        elif len(blocks) % 3 == 1:
            blocks.append(Block(x,y, "gray"))
        else:
            blocks.append(Block(x, y, "darkgray"))
screen.tracer(1)
update()

screen.exitonclick()
