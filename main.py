

import turtle as t 

#SCREEN

def initialize_screen():
    """Shows the screen of the game on the Terminal.

    specification:
        - Didiboo v1 (09/05/25)
    implementation:
        - Didiboo v1 (11/05/25)
    """
    screen = t.getscreen()
    
    screen.title("Nebulon Invasion: The Game")
    screen.setup(width=0.5, height=0.75, startx=None, starty=None)

    #Set the game background
    background = screen.bgpic('assets/space_invaders_background.png')

initialize_screen()

def set_timer():
    """Set timer.
    """

def set_score():
    """Set score.
    """

def set_frame_rate():
    """Set the game frame rate.
    """

#CANNON

def cannon_movement():
    """Moves the cannon on the screen.
    """

def create_cannon():
    """Creates the laser cannon.
    """
    laser_cannon = turtle.Turtle()

def laser_attack():
    """Shoots lasers at the aliens.
    """

#ALIENS

def create_aliens():
    """Creates aliens.
    """

def move_aliens():
    """Moves aliens across the screen.
    """

#GAME LOGIC

def game_start():
    """Initiate the game.
    """

def end_game():
    """Ends the game.
    """


#MAIN SCRIPT

#Keeps the window open
t.mainloop() 