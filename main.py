from tkinter import *  # for graphical user interface
from Utils import *  # Package
from PIL import ImageTk, Image  # For displaying images, installation command: pip install pillow


# Setting up window
app = Tk()
app.state('zoomed')
app.title("LIBRARY MANAGEMENT SYSTEM")
app.iconbitmap("assets/logo.ico")

# Creating variables
COLOURS = {'theme1': '#151517', 'theme2': 'white', 'theme3': '#202124', 'grey': '#9f9898'}
WIDTH, HEIGHT = app.winfo_width(), app.winfo_height()
SIDEBARWIDTH, SIDEBARHEIGHT = 270, HEIGHT - 3.8

# Creating canvas with background image
bg = Image.open("assets/bgimg.png")
bg = bg.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg)

canvas = Canvas(app, bd=0, width=WIDTH, height=HEIGHT, highlightbackground='black', bg='#8427d6')
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')
quote = canvas.create_text(0.5 * WIDTH, 0.425 * HEIGHT, fill="white", font=("gabriola", 50, 'bold'),
                           justify="center", width=WIDTH - SIDEBARWIDTH - 95, text='', activefill='yellow')
tur_cnvs = Canvas(canvas, width=250, height=40)  # Canvas for turtle screen

# --------- DISPLAY TAB ------------ #
# Search
search_f = Frame(canvas)
search_entry = Entry(search_f, width=45, font=("Comic Sans MS", 10), bg=COLOURS['grey'], fg='black', relief='ridge')
search_entry.grid(row=0, column=0, ipady=4)
search_img = ImageTk.PhotoImage(file="assets/search.png")
search_Button = Button(search_f, command=lambda: search(display, search_entry), image=search_img, padx=4)
search_Button.grid(row=0, column=1)

# Display box
display = Listbox(canvas, height=27, width=130, bg=COLOURS['theme3'], fg=COLOURS['theme2'],
                  font=("consolas", 10, "normal"), yscrollcommand=True, xscrollcommand=True)

# ---------- OTHER TABS ---------#
BOARD = Frame(canvas, padx=100, pady=100, bg=COLOURS['theme3'], highlightthickness=3,
              highlightbackground=COLOURS['theme1'], )
# Entry box labels
label1 = Label(BOARD, pady=10, bg=COLOURS['theme3'], fg=COLOURS['theme2'], font=("Consolas", 16, "bold"))
label2 = Label(BOARD, pady=10, bg=COLOURS['theme3'], fg=COLOURS['theme2'], font=("Consolas", 16, "bold"))
label3 = Label(BOARD, pady=10, bg=COLOURS['theme3'], fg=COLOURS['theme2'], font=("Consolas", 16, "bold"))
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
# Entry boxes
entrybox1 = Entry(BOARD, width=40, font=("Comic Sans MS", 10), bd=2)
entrybox2 = Entry(BOARD, width=40, font=("Comic Sans MS", 10), bd=2)
entrybox3 = Entry(BOARD, width=40, font=("Comic Sans MS", 10), bd=2)
entrybox1.grid(row=0, column=1, ipady=4)
entrybox2.grid(row=1, column=1, ipady=4)
entrybox3.grid(row=2, column=1, ipady=4)
# Options menu for update tab, for choosing field
item = StringVar()
item.set("--Select--")  # Default options
menu = OptionMenu(BOARD, item, "Book ID", "Book Name", "Author Name", "Patron ID")
menu.grid(row=1, column=1)
menu.config(font='consolas', bd=1, width=31)

# Buttons
ADD_Button = Button(BOARD, text='+ADD  ', padx=17, pady=1, command=lambda: add(BOARD_WIDGETS), bg='red',
                    fg=COLOURS['theme1'], font=('Helevetica', 13, 'bold'))
DEL_Button = Button(BOARD, text='DELETE', padx=17, pady=1, command=lambda: delete(BOARD_WIDGETS), bg='red',
                    fg=COLOURS['theme1'], font=('Helevetica', 13, 'bold'))
UPD_Button = Button(BOARD, text='UPDATE', padx=17, pady=1, command=lambda: update(BOARD_WIDGETS, item), bg='red',
                    fg=COLOURS['theme1'], font=('Helevetica', 13, 'bold'))
STATUS_Button = Button(BOARD, text='ISSUE', padx=17, pady=1, command=lambda: status(BOARD_WIDGETS, STATUS_Button),
                       bg='red', fg=COLOURS['theme1'], font=('Helevetica', 13, 'bold'))
ADD_Button.grid(row=3, column=1)
DEL_Button.grid(row=1, column=1)
UPD_Button.grid(row=3, column=1)
STATUS_Button.grid(row=2, column=1)

BOARD_WIDGETS = [BOARD, [label1, label2, label3], [entrybox1, entrybox2, entrybox3, menu],
                 [ADD_Button, DEL_Button, UPD_Button, STATUS_Button]]

# --------- SIDEBAR MENU -------------#
# Collapsible sidebar frame for showing options menu
sidebar = Frame(canvas, bg=COLOURS['theme1'], width=50, height=SIDEBARHEIGHT, relief='ridge', bd=1)
sidebar.place(x=0, y=2)
canvas.bind('<Button>', lambda e: contrast(e, sidebar))
# Menu collapsing Button
Button(canvas, bd=0, relief='ridge', fg='white', bg=COLOURS['theme1'], text='☰', font=("roman", 20, "normal"), command=lambda: collapse(sidebar, SIDEBARWIDTH), activebackground=COLOURS['theme1']).place(x=4, y=4)
# Sidebar Buttons
photo = ImageTk.PhotoImage(file="assets/logo.png")
icon = Button(sidebar, bd=0, bg=COLOURS['theme1'], image=photo, command=lambda: frontpg(widgets), activebackground=COLOURS['theme1'])
icon.place(x=0.23 * SIDEBARWIDTH, y=0.009 * SIDEBARHEIGHT)

PADX = 55
BD = 0
FG = COLOURS['theme2']
BG = COLOURS['theme1']
FONT = ("consolas", 15, "bold")
Y = 180
ANCHOR = 'center'
ACTIVEBACKGROUND = COLOURS['theme3']
show_B   = Button(sidebar, bd=BD, text="⬗  BOOK LIST    ", command=lambda: show(widgets), pady=5, fg=FG,
                  bg=BG, font=FONT, padx=PADX, anchor=ANCHOR, activebackground=ACTIVEBACKGROUND)
add_B    = Button(sidebar, bd=BD, text="⬖  ADD BOOK     ", command=lambda: add_tab(widgets), pady=5, fg=FG,
               bg=BG, font=FONT, padx=PADX, anchor=ANCHOR, activebackground=ACTIVEBACKGROUND)
delete_B = Button(sidebar, bd=BD, text="⬗  DELETE BOOK  ", command=lambda: delete_tab(widgets), pady=5, fg=FG,
                  bg=BG, font=FONT, padx=PADX, anchor=ANCHOR, activebackground=ACTIVEBACKGROUND)
update_B = Button(sidebar, bd=BD, text="⬖  UPDATE RECORD", command=lambda: update_tab(widgets), pady=5, fg=FG,
                  bg=BG, font=FONT, padx=PADX, anchor=ANCHOR, activebackground=ACTIVEBACKGROUND)
issue_B  = Button(sidebar, bd=BD, text="⬗  ISSUE BOOK   ", command=lambda: status_tab(widgets, 'ISSUE'), pady=5, fg=FG,
                  bg=BG, font=FONT, padx=PADX, anchor=ANCHOR, activebackground=ACTIVEBACKGROUND)
return_B = Button(sidebar, bd=BD, text="⬖  RETURN BOOK  ", command=lambda: status_tab(widgets, "RETURN"), fg=FG, pady=5,
                  bg=BG, font=FONT, padx=PADX, anchor=ANCHOR, activebackground=ACTIVEBACKGROUND)
patron_B = Button(sidebar, bd=BD, text="   😀PATRON       ", command=lambda: window(app), fg="red", pady=5,
                  bg=BG, font=FONT, padx=PADX, anchor=ANCHOR, activebackground=ACTIVEBACKGROUND)
show_B.place(x=0, y=Y + 25)
add_B.place(x=0, y=Y + 65)
delete_B.place(x=0, y=Y + 105)
update_B.place(x=0, y=Y + 145)
issue_B.place(x=0, y=Y + 185)
return_B.place(x=0, y=Y + 225)
patron_B.place(x=0,y=SIDEBARHEIGHT-100)

widgets = [[canvas, tur_cnvs], [search_f, display], quote, BOARD_WIDGETS, sidebar, SIDEBARWIDTH]
app.update()
frontpg(widgets)  # Showing front page on starting
app.mainloop()
