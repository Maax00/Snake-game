from food import Food
from snake import Snake
from turtle import Turtle

ALIGN = "center"
FONT = ("arial", 20, "normal")

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt", "r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Your score is: {self.current_score} Highscore: {self.highscore}", align= ALIGN, font=FONT)

    def new_game(self):
        if self.current_score > self.highscore:
            self.highscore = self.current_score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.highscore}")
        self.current_score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Your score is: {self.current_score} Highscore: {self.highscore}", align= ALIGN, font=FONT)

    def add_point(self):
        self.current_score += 1

        self.write(f"Your score is: {self.current_score} Highscore: {self.highscore}", align= ALIGN, font=FONT)


