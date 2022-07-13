import winsound, turtle
from tkinter import *
from tkinter import messagebox
from random import choice
import mysql.connector

# Creating front  page
quotes = ['“A reader lives a thousand lives before he dies.”\n\t-George R.R Martin',
          '“Show me a family of readers, and I will show you the people who move the world.”\n\t –Napoleon Bonaparte',
          '“A book is a garden, an orchard, a storehouse, a party, a company by the way, a counselor, a multitude of counselors.”\n\t – Charles Baudelaire']

def frontpg(wd: list):
    forget(wd[0]+wd[1]+[wd[3][0]])
    canvas=wd[0][0]
    canvas.itemconfig(wd[2], text=choice(quotes))

# Collapsing sidebar by adjusting width
def collapse(sidebar: Frame, SIDEBARWIDTH: float):
    if sidebar['width'] == SIDEBARWIDTH:    sidebar.config(width=50, padx=50)
    else:   sidebar.config(width=SIDEBARWIDTH, padx=0)

def contrast(event,sidebar):  sidebar.config(width=50, padx=50)

# Clearing screen by hiding widgets
def forget(wd: list, lay_mngr="place"):
    for widget in wd:
        if   lay_mngr == "place":   widget.place_forget()
        elif lay_mngr == "grid":    widget.grid_forget()


# Placing required widgets
def unforget(wd: list, pos: tuple, lay_mngr="place"):
    for i in range(len(wd)):

        if lay_mngr == "place":
            wd[i].place(relx=pos[i][0], rely=pos[i][1])
        elif lay_mngr == "grid":
            if len(pos[i]) == 2:
                wd[i].grid(row=pos[i][0], column=pos[i][1])
            else:
                wd[i].grid(row=pos[i][0], column=pos[i][1], ipady=pos[i][2])


# Playing sound with winsound
def sound(audio="completion"):
    if audio == "completion":
        winsound.PlaySound("assets/beep.wav", winsound.SND_ALIAS)


# Pop-up message box
def msgbox(msg: str, msg_type: int, title="LIBRARY MANAGEMENT SYSTEM"):
    if msg_type == -1: # Error message
        messagebox.showerror(title, msg)
    elif msg_type == 0 : # warning message
        messagebox.showwarning(title, msg)
    elif msg_type == 1: # Confirmation
        ans =messagebox.askyesno(title, msg)
        return ans

# Writing heading with turtle animation
def write_name(canvas: Canvas, txt: str, bg="#202124"):
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor(bg)
    pen = turtle.RawTurtle(screen, shape="circle")
    pen.hideturtle()
    pen.clear()
    pen.hideturtle()
    pen.pencolor("red")
    pen.penup()
    pen.goto(-120, -15)
    pen.speed(3)
    for char in txt:
        pen.write(char, align="left", move=True, font=("ROG Fonts", 25, "normal"))
        pen.forward(1)
