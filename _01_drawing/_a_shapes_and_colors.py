import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    turtle_league = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    turtle_league.shape('turtle')
    # Set your turtle's speed using .speed(2)
    turtle_league.speed(5)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    turtle_league.color("#889feb")
    # Move your turtle forward using .forward(100)
    for i in range(4):
        turtle_league.forward(200)
        turtle_league.right(90)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.

    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    turtle_league.goto(0,0)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    turtle_league.begin_fill()
    turtle_league.circle(50, 360)
    turtle_league.end_fill()
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    turtle_league.color("#912929")
    turtle_league.begin_fill()
    turtle_league.penup()
    turtle_league.goto(250,250)
    turtle_league.pendown()
    for i in range(9):
        turtle_league.forward(50)
        turtle_league.right(40)
    turtle_league.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
