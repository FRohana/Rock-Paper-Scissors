# This file was created by Farid Rohana

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
have t

'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint
from time import sleep
# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')

# Used this resource to include sound
# https://www.youtube.com/watch?v=w6g8PO-Pqp4
def play_rock():
    winsound.PlaySound(os.path.join(sounds_folder, 'rock.wav'), winsound.SND_ASYNC)
def play_paper():
    winsound.PlaySound(os.path.join(sounds_folder, 'paper.wav'), winsound.SND_ASYNC)
def play_scissors():
    winsound.PlaySound(os.path.join(sounds_folder, 'scissors.wav'), winsound.SND_ASYNC)

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

player_choice = ""

cpu_choice = ""

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="orange")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
# rock_instance.hideturtle()

cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()
# cpu_rock_instance.hideturtle()

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
# paper_instance.hideturtle()

cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()
# cpu_paper_instance.hideturtle()


scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
# scissors_instance.hideturtle()

cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()
# cpu_scissors_instance.hideturtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    # add the cpu_rock_image as a shape
    screen.addshape(cpu_rock_image)
    # attach the cpu_rock_image to the cpu_rock_instance
    cpu_rock_instance.shape(cpu_rock_image)
    # remove the pen option from the cpu_rock_instance so it doesn't draw lines when moved
    cpu_rock_instance.penup()
    # set the position of the cpu_rock_instance
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    # add the paper_image as a shape
    screen.addshape(paper_image)
    # attach the paper_image to the paper_instance
    paper_instance.shape(paper_image)
    # remove the pen option from the paper_instance so it doesn't draw lines when moved
    paper_instance.penup()
    # set the position of the paper_instance
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    # add the cpu_paper_image as a shape
    screen.addshape(cpu_paper_image)
    # attach the cpu_paper_image to the cpu_paper_instance
    cpu_paper_instance.shape(cpu_paper_image)
    # remove the pen option from the cpu_paper_instance so it doesn't draw lines when moved
    cpu_paper_instance.penup()
    # set the position of the cpu_paper_instance
    cpu_paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(cpu_scissors_image)
    cpu_scissors_instance.penup()
    cpu_scissors_instance.setpos(x,y)


text = turtle.Turtle()

# Defines text characteristics 
def write_text(message, x, y):
    text.hideturtle()
    text.color('black')
    text.penup()
    text.clear()
    text.setpos(x,y)
    text.write(message, False, "center", ("Arial", 24, "normal"))
    # for i in message:
    #     text.setpos(x,y)
    #     text.write(i, False, "center", ("Arial", 24, "normal"))    
    #     x += 17
    #     sleep(.01)


# Writes opeining text on the top of the window 
write_text("Choose rock, paper, or scissors...", 0, 150 )
        

def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]

# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)

# function that passes through wn onlick
def mouse_pos(x, y):
    print(cpu_select())
    cpu_picked = cpu_select()
    # Determines sequences when you pick rock
    if collide(x,y,rock_instance,rock_w,rock_h):  
        write_text("You picked the ROCK!", 0, 150 )
        play_rock()
        if cpu_picked == "rock":
            show_scissors(2000,0)
            show_paper(2000,0)
            cpu_show_rock(300,0)
            show_rock(-300,0)
            write_text("It is a tie...", 0, 150 )
        if cpu_picked == "paper":
            show_scissors(2000,0)
            show_paper(2000,0)
            cpu_show_paper(300,0)
            show_rock(-300,0)
            write_text("You lost!", 0, 150 ) 
        if cpu_picked == "scissors":
            show_scissors(2000,0)
            show_paper(2000,0)
            cpu_show_scissors(300,0)
            show_rock(-300,0)
            write_text("you win!", 0, 150 )       
    # Determines sequences when you pick paper
    elif collide(x,y,paper_instance,paper_w,paper_h):
        write_text("You picked the PAPER!", 0, 150 )
        play_paper()
        if cpu_picked == "rock":
            show_rock(2000,0)
            show_scissors(2000,0)
            show_paper(-300,0)
            cpu_show_rock(300,0)
            write_text("You win!", 0, 150 )
        if cpu_picked == "paper":
            show_scissors(2000,0)
            show_rock(2000,0)
            show_paper(-300,0)
            cpu_show_paper(300, 0)
            write_text("It is a tie...", 0, 150 )
        if cpu_picked == "scissors":
            show_rock(2000,0)
            show_scissors(2000,0)
            show_paper(-300,0)
            cpu_show_scissors(300,0)
            write_text("you lose!", 0, 150 )  
    # Determines sequences when you pick scissors
    elif collide(x,y,scissors_instance,scissors_w,scissors_h):
        write_text("You picked the SCISSORS!", 0, 150 )
        play_scissors()
        if cpu_picked == "rock":
            show_paper(2000,0)
            show_rock(2000,0)
            show_scissors(-300,0)
            cpu_show_rock(300,0)
            write_text("You lost!", 0, 150 )
        if cpu_picked == "paper":
            show_paper(2000,0)
            show_rock(2000,0)
            show_scissors(-300,0)
            cpu_show_paper(300,0)
            write_text("You win!", 0, 150 ) 
        if cpu_picked == "scissors":
            show_rock(2000,0)
            show_paper(2000,0)
            show_scissors(-300,0)
            cpu_show_scissors(300,0)
            write_text("Its a tie...", 0, 150 )   
    else:
        write_text("You clicked on NOTHING!", 0, 150 )

screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last  


screen.mainloop()

