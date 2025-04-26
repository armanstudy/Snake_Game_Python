from turtle import Turtle, Screen
import random

class Food(Turtle):
    """Class representing the food in the snake game."""

    def __init__(self):
        """Initialize the food object."""
        super().__init__()  # Call the constructor of the parent class (Turtle)
        self.shape("circle")  # Set the shape of the food to a circle
        self.color("blue")  # Set the color of the food to blue
        self.penup()  # Prevent drawing lines when moving
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")  # Set the speed of the turtle to fastest
        self.refresh()

        
    def refresh(self):
        """Place the food at a random position on the screen."""
        x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen bounds
        y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen bounds
        self.goto(x, y)  # Move the food to the random position

