# Import turtle module for its functionality
from turtle import Turtle
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    """
    Responsible for creating a scoreboard to show scores and partition among players
    """

    def __init__(self):
        super().__init__()
        # Create a scoreboard with specific properties and behaviors
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.draw_middle_line()
        self.update_scoreboard()

    def draw_middle_line(self):
        """
        Draws the line at the middle of the screen for the partition among both players.
        """
        line = Turtle()
        line.pensize(5)
        line.color("white")
        line.penup()
        line.goto(0, 300)
        line.setheading(270)
        # Draw a line from up to down on the screen
        while line.ycor() > -280:
            line.pendown()
            line.forward(10)
            line.penup()
            line.forward(20)
        line.hideturtle()

    def update_scoreboard(self):
        """
        Clears the previous score and writes the updated score on the scoreboard.
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        """
        Increments the score of the left player and updates the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increments the score of the right player and updates the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()
