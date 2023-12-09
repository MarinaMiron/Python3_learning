from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("Day20\data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg= f"Score: {self.score} High score: {self.high_score}", align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day20\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg= "GAME OVER.", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()