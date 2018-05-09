import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("#E80E0E")
wn.title("Turtle graphics game")


class Game(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(-290, 310)
        self.score = 0

    def update_score(self):
        self.clear()
        self.write("Your Score: {}".format(self.score), False, align="left", font=("Arial", 14, "normal"))

    def change_score(self, points):
        self.score += points
        self.update_score()

class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.speed = 1

    def move(self):
        self.forward(self.speed)
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

    def turn_left(self):
        self.left(30)

    def turn_right(self):
        self.right(30)

    def increase_speed(self):
        self.speed += 1

class Goal(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("black")
        self.speed = 3
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0,360))

    def jump(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)


def isCollision(t1,t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2)) #pythagorean theorem to measure distance

    if distance < 20:
        return True
    else:
        return False

player = Player()
border = Border()
game = Game()

goals = []

for i in range(6):
    goals.append(Goal())

border.draw_border()

wn.listen()
wn.onkey(player.turn_left, "Left")
wn.onkey(player.turn_right, "Right")
wn.onkey(player.increase_speed, "Up")

wn.tracer(0)

while True:
    wn.update()
    player.move()

    for goal in goals:
        goal.move()

        if isCollision(player, goal):
            goal.jump()
            game.change_score(10)