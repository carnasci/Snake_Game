from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Currier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        with open("data.txt", "r") as file:
            highscore = file.read()
        self.score = 0
        self.high_score = int(highscore)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
