from tkinter import*
import turtle
import time

WIDTH, HEIGHT = 700, 400

root = Tk()
x = root.winfo_screenwidth()/2 - WIDTH/2
y = root.winfo_screenheight()/2 -HEIGHT/2
root.geometry(f"{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}")
root.config(highlightthickness=0)
root.overrideredirect(True)

# Turtle
canvas = Canvas(root, width=WIDTH, height=HEIGHT,highlightthickness=0)
canvas.pack(expand=1, fill=BOTH, anchor='sw')
screen = turtle.TurtleScreen(canvas)
screen.bgpic("assets/bg.png")
# Writing heading
splash = turtle.RawTurtle(screen,"square")
splash.speed(0)
splash.shapesize(0.7)
splash.color("red")
splash.hideturtle()
splash.penup()
splash.left(180)
splash.fd(300)
splash.right(90)
splash.pendown()
splash.write("LIBRARY MANAGEMENT\n" + " "*15 +"SYSTEM", font=("rog fonts", 30, "bold"))
# Moving turtle to bottom-left
splash.penup()
splash.pensize(15)
splash.goto(-WIDTH/2,-HEIGHT/2)
splash.speed(1)
splash.right(90)
splash.showturtle()
splash.pendown()
# Loading
splash.fd(WIDTH/2)
splash.fd(WIDTH/3)
time.sleep(2)
splash.fd(WIDTH/6)
root.destroy()

root.mainloop()
