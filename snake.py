from turtle import Turtle

SEGMENT_LOCATIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20  # Distance to move the snake each time

UP = 90  # Angle to move up
DOWN = 270  # Angle to move down
LEFT = 180  # Angle to move left
RIGHT = 0  # Angle to move right

class Snake:
    def __init__(self):
        self.segments = []  # List to store the snake segments
        self.create_snake()  # Create the initial snake

    def create_snake(self):
        """Create the initial snake with three segments."""
        for position in SEGMENT_LOCATIONS:
            self.add_segment(position)  # Add each segment at the specified position

    def add_segment(self, position):
        """Add a new segment to the snake at the given position."""
        new_segment = Turtle("square")  # Create a new turtle segment
        new_segment.color("white")  # Set the color of the segment to white
        new_segment.penup()  # Prevent drawing lines when moving
        new_segment.goto(position)  # Move the segment to the specified position
        self.segments.append(new_segment)  # Add the segment to the list of segments

    def extend(self):
        """Extend the snake by adding a new segment at the end."""
        self.add_segment(self.segments[-1].position())  # Add a new segment at the last segment's position

    # The following methods control the movement of the snake in different directions.
    # These methods set the heading of the snake's head segment to the corresponding angle.
    # The snake will move in the direction of its head. 
    def move(self):
        """Move the snake forward by updating each segment's position."""
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from the last segment and move backward
            x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment
            self.segments[seg_num].goto(x, y)  # Move the current segment to the previous segment's position

        self.segments[0].forward(MOVE_DISTANCE)  # Move the head of the snake forward by MOVE_DISTANCE
    
    
    def up(self):
        """Change direction to up if not already moving down."""
        self.segments[0].setheading(UP)  # Set heading to up

    def down(self):
        """Change direction to down if not already moving up."""
        self.segments[0].setheading(DOWN)  # Set heading to down
    
    def left(self):
        """Change direction to left if not already moving right."""
        self.segments[0].setheading(LEFT)   # Set heading to left   
    
    def right(self):            
        """Change direction to right if not already moving left."""
        self.segments[0].setheading(RIGHT)  # Set heading to right


      