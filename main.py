
import turtle as t 


#GAME SCREEN

t.title("SPACE INVADERS: THE GAME")
screen = t.Screen()

screen.tracer(0) # unable auto-update

t.hideturtle() #hides default turtle

#screen settings
screen.bgcolor("#211e20")
t.setup(width=0.5, height=0.75)

left = - screen.window_width() / 2
right = screen.window_width() / 2
top = screen.window_height() / 2
bottom = - screen.window_height() / 2
cannon_zone = bottom * 0.9
border = screen.window_width() * 0.025

# CANNON SETTINGS
cannon = t.Turtle()
cannon.penup()
cannon.color("#555568")
cannon.shape("square")
cannon.setpos(0, cannon_zone)

# cannon design
def draw_cannon():
    """Draws the laser cannon.

    Version
    -------
        - Didiboo v1 (22/06/25)
        - Didiboo v2 (24/06/25)
    """
    cannon.clear()
    cannon.turtlesize(1, 4)  # Base
    cannon.stamp()
    cannon.sety(cannon_zone + 10)
    cannon.turtlesize(1, 1.5)  # Next tier
    cannon.stamp()
    cannon.sety(cannon_zone + 20)
    cannon.turtlesize(0.8, 0.3)  # Tip of cannon
    cannon.stamp()
    cannon.sety(cannon_zone)

# CANNON MOVEMENTS
step = 10

def move_right():
    """Moves the cannon to the right.

    Version
    -------
        - Didiboo v1 (22/06/25)
    """
    new_x = cannon.xcor() + step

    if new_x <= right - border:
        cannon.setx(new_x)
        draw_cannon()

def move_left():
    """Moves the cannon to the left.

    Version
    -------
        - Didiboo v1 (22/06/25)
    """
    new_x = cannon.xcor() - step

    if new_x >= left + border:
        cannon.setx(new_x)
        draw_cannon()

# LASER

lasers = []

def create_lasers():
    """Creates the lasers.

    Version
    -------
        - Didiboo (24/06/25)
    """
    laser = t.Turtle()

    # laser design
    laser.penup()
    laser.color("#e9efec")

    laser.hideturtle()

    #position
    laser.setposition(cannon.xcor(), cannon.ycor())

    # movement
    laser.setheading(90)
    laser.forward(20) # laser start at the tip of the cannon

    laser.pendown() #
    laser.pensize(5)

    #add laser to list
    lasers.append(laser)

    print(len(lasers))

laser_speed = 2
laser_length = 20

def move_laser(laser):
    """Moves the laser forwards.

    Parameter
    ---------
    laser : str
        Laser of the cannon.
    
    Version
    -------
        - Didiboo v1 (24/06/25)
    """
    laser.clear()
    laser.forward(laser_speed)
    # Draw the laser
    laser.forward(laser_length)
    laser.forward(-laser_length)


# bind key to actions
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.onkeypress(screen.bye, "q")
screen.onkeypress(create_lasers, "space")
screen.listen()

# GAME LOOP
while True:
    for laser in lasers:
        move_laser(laser)

        if laser.ycor() > top:
            # make sure that the laser is no longer visible
            laser.clear()
            laser.hideturtle()

            lasers.remove(laser) # removes the laser from the list
            t.turtles().remove(laser) # removes the laser from the internal list of all Turtle objects
    
    screen.update() # update manually the screen

#Keeps the window open
t.mainloop() 