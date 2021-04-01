from turtle import Turtle

WIDTH = 20
HEIGHT = 100
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
