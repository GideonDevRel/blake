import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Doraemon Drawing")
screen.setup(width=800, height=600)

# Create a turtle
pen = turtle.Turtle()
pen.speed(8)

def draw_circle(radius, color="black", fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        pen.fillcolor(fill_color)
        pen.begin_fill()
    pen.circle(radius)
    if fill_color:
        pen.end_fill()

def move_to(x, y):
    """Move to position without drawing"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def draw_head():
    """Draw Doraemon's head"""
    # Main head circle (blue)
    move_to(0, -100)
    pen.color("black", "#0099FF")
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    
    # Face area (white)
    move_to(0, -70)
    pen.color("black", "white")
    pen.begin_fill()
    pen.circle(70)
    pen.end_fill()

def draw_eyes():
    """Draw Doraemon's eyes"""
    # Left eye
    move_to(-25, 20)
    pen.color("black", "white")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()
    
    # Left pupil
    move_to(-25, 25)
    pen.color("black", "black")
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()
    
    # Right eye
    move_to(25, 20)
    pen.color("black", "white")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()
    
    # Right pupil
    move_to(25, 25)
    pen.color("black", "black")
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()

def draw_nose():
    """Draw Doraemon's nose"""
    move_to(0, 10)
    pen.color("black", "#FF0000")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

def draw_mouth():
    """Draw Doraemon's mouth"""
    # Mouth line from nose
    move_to(0, 5)
    pen.color("black")
    pen.pensize(3)
    pen.setheading(270)  # Point downward
    pen.forward(20)
    
    # Mouth curve
    pen.setheading(225)
    pen.circle(20, 90)
    
    # Reset pen
    pen.pensize(1)

def draw_whiskers():
    """Draw Doraemon's whiskers"""
    pen.color("black")
    pen.pensize(2)
    
    # Left whiskers
    for i, y_pos in enumerate([5, -5, -15]):
        move_to(-60, y_pos)
        pen.setheading(0)
        pen.forward(30)
    
    # Right whiskers
    for i, y_pos in enumerate([5, -5, -15]):
        move_to(30, y_pos)
        pen.setheading(0)
        pen.forward(30)
    
    pen.pensize(1)

def draw_body():
    """Draw Doraemon's body"""
    # Main body (blue)
    move_to(0, -100)
    pen.color("black", "#0099FF")
    pen.begin_fill()
    pen.setheading(270)
    pen.forward(120)
    pen.circle(80, 180)
    pen.forward(120)
    pen.end_fill()
    
    # Belly (white)
    move_to(0, -110)
    pen.color("black", "white")
    pen.begin_fill()
    pen.setheading(270)
    pen.forward(100)
    pen.circle(60, 180)
    pen.forward(100)
    pen.end_fill()

def draw_pocket():
    """Draw Doraemon's pocket"""
    move_to(0, -150)
    pen.color("black", "white")
    pen.begin_fill()
    pen.setheading(0)
    pen.circle(25, 180)
    pen.end_fill()
    
    # Pocket opening
    move_to(-25, -150)
    pen.color("black")
    pen.pensize(3)
    pen.setheading(0)
    pen.forward(50)
    pen.pensize(1)

def draw_arms():
    """Draw Doraemon's arms"""
    # Left arm
    move_to(-80, -120)
    pen.color("black", "#0099FF")
    pen.begin_fill()
    pen.setheading(225)
    pen.circle(25, 180)
    pen.end_fill()
    
    # Left hand
    move_to(-100, -140)
    pen.color("black", "white")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()
    
    # Right arm
    move_to(80, -120)
    pen.color("black", "#0099FF")
    pen.begin_fill()
    pen.setheading(315)
    pen.circle(25, 180)
    pen.end_fill()
    
    # Right hand
    move_to(100, -140)
    pen.color("black", "white")
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()

def draw_legs():
    """Draw Doraemon's legs"""
    # Left leg
    move_to(-30, -220)
    pen.color("black", "#0099FF")
    pen.begin_fill()
    pen.setheading(270)
    pen.forward(40)
    pen.setheading(0)
    pen.forward(20)
    pen.setheading(90)
    pen.forward(40)
    pen.setheading(180)
    pen.forward(20)
    pen.end_fill()
    
    # Left foot
    move_to(-40, -260)
    pen.color("black", "white")
    pen.begin_fill()
    pen.setheading(0)
    pen.forward(40)
    pen.circle(10, 90)
    pen.forward(10)
    pen.circle(10, 90)
    pen.forward(40)
    pen.setheading(90)
    pen.forward(20)
    pen.end_fill()
    
    # Right leg
    move_to(30, -220)
    pen.color("black", "#0099FF")
    pen.begin_fill()
    pen.setheading(270)
    pen.forward(40)
    pen.setheading(180)
    pen.forward(20)
    pen.setheading(90)
    pen.forward(40)
    pen.setheading(0)
    pen.forward(20)
    pen.end_fill()
    
    # Right foot
    move_to(0, -260)
    pen.color("black", "white")
    pen.begin_fill()
    pen.setheading(0)
    pen.forward(40)
    pen.circle(10, 90)
    pen.forward(10)
    pen.circle(10, 90)
    pen.forward(40)
    pen.setheading(90)
    pen.forward(20)
    pen.end_fill()

def draw_collar():
    """Draw Doraemon's collar with bell"""
    # Collar
    move_to(-50, -100)
    pen.color("black", "#FF0000")
    pen.pensize(8)
    pen.setheading(0)
    pen.forward(100)
    
    # Bell
    move_to(0, -95)
    pen.color("black", "#FFD700")
    pen.pensize(1)
    pen.begin_fill()
    pen.circle(8)
    pen.end_fill()
    
    # Bell line
    move_to(-3, -95)
    pen.color("black")
    pen.pensize(1)
    pen.setheading(0)
    pen.forward(6)

def main():
    """Main function to draw Doraemon"""
    pen.hideturtle()  # Hide the turtle cursor
    
    # Draw all parts
    draw_head()
    draw_eyes()
    draw_nose()
    draw_mouth()
    draw_whiskers()
    draw_body()
    draw_pocket()
    draw_arms()
    draw_legs()
    draw_collar()
    
    # Add signature
    move_to(-300, -280)
    pen.color("gray")
    pen.write("Doraemon - Created with Python Turtle", font=("Arial", 12, "normal"))
    
    # Keep the window open
    screen.exitonclick()
    print("Click on the window to close it!")

if __name__ == "__main__":
    main()