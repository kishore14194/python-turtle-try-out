import turtle
import random

wn = turtle.Screen()
wn.bgcolor("#E80E0E")
wn.title("Turtle graphics game")


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

    def move(self):
        self.forward(self.speed)
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)


player = Player()
border = Border()
goal = Goal()

border.draw_border()

wn.listen()
wn.onkey(player.turn_left, "Left")
wn.onkey(player.turn_right, "Right")
wn.onkey(player.increase_speed, "Up")

while True:
    player.move()
    goal.move()