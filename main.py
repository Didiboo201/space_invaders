
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

    screen.update() # update manually the screen

# cannon movements
step = 10

def move_right():
    """Moves the cannon to the right.
    """
    new_x = cannon.xcor() + step

    if new_x <= right - border:
        cannon.setx(new_x)
        draw_cannon()

def move_left():
    """Moves the cannon to the left.
    """
    new_x = cannon.xcor() - step

    if new_x >= left + border:
        cannon.setx(new_x)
        draw_cannon()


# bind key to motion
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")
screen.onkeypress(screen.bye, "q")
screen.listen()

#Keeps the window open
t.mainloop() 