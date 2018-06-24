import turtle
import time

wn = turtle.Screen()
wn.title("Traffic lights")
wn.bgcolor("black")

# Draw box for signal

pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red Light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0,40)
# pen.pendown()

# yellow Light
yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0,0)
# pen.pendown()

# green Light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0,-40)
# pen.pendown()

while True:
    yellow_light.color("grey")
    red_light.color("red")
    time.sleep(4)

    red_light.color("grey")
    green_light.color("green")
    time.sleep(2)

    green_light.color("grey")
    yellow_light.color("yellow")
    time.sleep(1)

wn.mainloop()