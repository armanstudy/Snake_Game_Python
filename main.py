# Import necessary modules
from turtle import Screen, Turtle  # Import the Screen and Turtle classes from the turtle module
import time

# Import custom classes
from snake import Snake  # Handles the snake's movement, growth, and direction changes
from foods import Food   # Manages the food's appearance and position
from scoreboard import Scoreboard  # Displays the score and game-over message

# Set up the game screen
screen = Screen()
screen.setup(width=800, height=600)  # Set the screen size
screen.title("SNAKE GAME")           # Set the game title
screen.bgcolor("black")              # Set the background color
screen.tracer(0)                     # Turn off automatic screen updates for better performance
screen.listen()                      # Enable key event listening


# Initialize game objects
snake = Snake()                      # Create the snake
food = Food()                        # Create the food
scoreboard = Scoreboard()            # Create the scoreboard


# Bind arrow keys to snake movement
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True  # Flag to control the game loop
while  game_is_on:
        screen.update()                  # Refresh the screen
        time.sleep(0.1)                  # Control the game speed
        snake.move()                  # Move the snake forward

        # Detect collision with food
        if snake.segments[0].distance(food) < 15:
            food.refresh()               # Reposition the food
            snake.extend()               # Extend the snake's body
            scoreboard.increase_score()  # Update the score

        # Detect collision with walls
        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with itself
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()  # Exit the game when the screen is clicked