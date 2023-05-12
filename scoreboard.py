from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"
SCORE_COORDINATES = (-200, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(SCORE_COORDINATES)
        self.color("black")
        self.level = 1
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def new_board(self):
        self.level += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align=ALIGN, font=FONT)
