from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.outline_game()

    def outline_game(self):
        tim = Turtle(shape="turtle")
        tim.hideturtle()
        tim.color("white")
        tim.penup()

        tim.setheading(90)
        tim.forward(260)

        tim.pendown()

        tim.setheading(0)
        tim.forward(280)

        tim.setheading(270)
        tim.forward(280)
        tim.forward(260)

        tim.setheading(180)
        tim.forward(280)
        tim.forward(280)

        tim.setheading(90)
        tim.forward(280)
        tim.forward(260)

        tim.setheading(0)
        tim.forward(280)
