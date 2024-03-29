from turtle import Turtle


class Score (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hight_score = self.get_hight_score()
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"The score is {self.score} High Score : {self.high_score}",
                   align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("C:/Code/Project/100-Day-Python-Project/Day24_HIgh_score_snake_game/score.txt", mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over",
    #                align='center', font=('Arial', 24, 'normal'))

    def get_hight_score(self):
        with open("C:/Code/Project/100-Day-Python-Project/Day24_HIgh_score_snake_game/score.txt", mode='r') as f:
            self.high_score = f.read()

            return self.high_score
