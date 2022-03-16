from tkinter import *
import random
from turtle import window_height

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
BODY_PARTS = 3
SPACE_SIZE = 50
BACKGROUND_COLOR = "#000000"
FOOD_COLOR = "#FF0000"
SNAKE_COLOR = "#00FF00"


class Snake:
    def __init__(self) -> None:
        pass


class Food:
    def __init__(self) -> None:
        pass


def next_turn():
    pass


def change_directiion(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

#settings of interface
interface = Tk()
interface.title("Bro_snake")
interface.resizable(0,0)

#score_label
score = 0
score_label = Label(interface, text="Score:{}".format(score), font=("consolas", 40))
score_label.pack()

#game arena
arena = Canvas(interface, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
arena.pack()

#interface geometry
interface.update()
screen_width = interface.winfo_screenwidth()
screen_height = interface.winfo_screenheight()
interface_height = interface.winfo_height()
interface_width = interface.winfo_width()

x = int((screen_width/2) - (interface_width/2))
y = int((screen_height/2) - (interface_height/2))

interface.geometry(f"{interface_width}x{interface_height}+{x}+{y}")
interface.mainloop()