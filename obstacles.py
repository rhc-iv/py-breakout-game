from turtle import Turtle

colors = ['#61AFEF', '#98C379', '#BE5046', '#E5C07B']


class Blocks(Turtle):

    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=5)
        self.goto(position)
        self.x_pos = -335
        self.y_pos = 50