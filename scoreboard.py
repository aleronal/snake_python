from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setx(0)
        self.sety(250)

    def update_score(self):
        self.write(arg="Score " + str(self.score), align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font= FONT)