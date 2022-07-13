from .Commonfunc import *
import mysql.connector
from tabulate import tabulate

def validate(value,type):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='pass123', database='LIBRARY_RECORDS')
    my_cursor = mydb.cursor()
    if type=="primary":
        my_cursor.execute("SELECT * FROM patron"); data = list(my_cursor.fetchall())
        for rec in data:
            if rec[0] == value: return True
        else: return False
    elif type=="name":
        my_cursor.execute("SELECT * FROM patron"); data = list(my_cursor.fetchall())
        for rec in data:
            if rec[0] == value: return rec[1]
    elif type=="int":
        if value.isdigit(): return True
        return False

def display():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='pass123', database='LIBRARY_RECORDS')
    my_cursor = mydb.cursor()

    my_cursor.execute("SELECT * FROM patron")
    data = list(my_cursor.fetchall())
    data = [("Patron ID","Name","Age","Email ID||")]+data
    my_cursor.close()
    mydb.close()
    return tabulate(data,tablefmt="plain")


def AddRec(id,name,age,email,Did):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='pass123', database='LIBRARY_RECORDS')
    my_cursor = mydb.cursor()
    if validate(id.get(),"int") or validate(age.get(),"int"):
        if not validate(int(id.get()),"primary"):
            my_cursor.execute("INSERT INTO patron VALUES(%s, %s, %s, %s)", (int(id.get()), name.get().title(), int(age.get()), email.get().lower()) )
            mydb.commit()
            sound()
        else: msgbox("Patron ID already exists,\nenter a different one.",-1)
    else:   msgbox("Invalid entry.\nPatron ID and age should be an integer ",-1)

    id.delete(0,"end"); name.delete(0,"end"); age.delete(0,"end"); email.delete(0,"end")
    my_cursor.close()
    mydb.close()


def DeleteRec(Did):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='pass123', database='LIBRARY_RECORDS')
    my_cursor = mydb.cursor()
    if validate(Did.get(),"int"):
        if validate(int(Did.get()),"primary"):
            my_cursor.execute("DELETE FROM patron WHERE PatronID = %s", (int(Did.get()),) )
            mydb.commit()
            sound()
        else: msgbox("Incorrect Patron ID.",-1)
    else: msgbox("Invalid entry.\nPatron ID and age should be an integer ",-1)
    Did.delete(0,"end")

    my_cursor.close()
    mydb.close()

def changeframe(frame,frames,box=None):
    for f in frames: f.grid_forget()
    frame.grid(row=1, column=0)
    if frame==frames[0]:
        data = display()
        data = data.replace(".com",".com||")
        data = data.split("||")
        box.delete(0, "end")
        for x in range(len(data)): box.insert("end",data[x])
        box.itemconfig(0, {'fg':'red', 'bg':'black'})


def window(root):
        win = Toplevel(root,bg="#2c3647",padx=50)
        win.geometry("640x390")
        # Frames
        showframe = Frame(win,width=270,height=270,padx=30,pady=20,bg="#37465e")
        addframe = Frame(win,width=270,height=270,padx=80,pady=50,bg="#37465e")
        deleteframe = Frame(win,width=270,height=270,padx=80,pady=60,bg="#37465e")
        frames = [showframe,addframe,deleteframe]
        # Frame widgets
        displaybox = Listbox(showframe, height=15, width=60, bg="#151517", fg="white",
                    font=("consolas", 11, "normal"), yscrollcommand=True, xscrollcommand=True); displaybox.pack()
        Label(addframe,text="Patron ID ",pady=10,bg="#37465e",font=("Consolas", 13, "normal"),fg="white").grid(row=0,column=0)
        id = Entry(addframe,width=30, font=("Comic Sans MS", 10), bd=2); id.grid(row=0,column=1,ipady=3)
        Label(addframe,text="Name      ",pady=10,bg="#37465e",font=("Consolas", 13, "normal"),fg="white").grid(row=1,column=0)
        name = Entry(addframe,width=30, font=("Comic Sans MS", 10), bd=2); name.grid(row=1,column=1,ipady=3)
        Label(addframe,text="Age       ",pady=10,bg="#37465e",font=("Consolas", 13, "normal"),fg="white").grid(row=2,column=0)
        age = Entry(addframe,width=30, font=("Comic Sans MS", 10), bd=2); age.grid(row=2,column=1,ipady=3)
        Label(addframe,text="Email ID  ",pady=10,bg="#37465e",font=("Consolas", 13, "normal"),fg="white").grid(row=3,column=0)
        email = Entry(addframe,width=30, font=("Comic Sans MS", 10), bd=2); email.grid(row=3,column=1,ipady=3)
        add_B = Button(addframe,text="Add",fg="black",bg="red", font="bold", command=lambda: AddRec(id,name, age,email,Did))
        add_B.grid(row=4,column=1)

        Label(deleteframe,text="Patron ID",pady=10,bg="#37465e",font=("Consolas", 13, "normal"),fg="white").grid(row=0,column=0)
        Did = Entry(deleteframe,width=30, font=("Comic Sans MS", 10), bd=2); Did.grid(row=0,column=1,ipady=3)
        del_B = Button(deleteframe,text="Delete",fg="black",bg="red", font="bold", command=lambda: DeleteRec(Did))
        del_B.grid(row=2,column=1)

        # Buttons
        group = Frame(win,padx=100,bg="#2c3647")
        add = Button(group,fg="blue",bg="black",font=("gabriola",15,"bold"),text=" +Add  ",command=lambda: changeframe(addframe,frames))
        delete = Button(group,fg="green",bg="black",font=("gabriola",15,"bold"),text=" Delete",command=lambda: changeframe(deleteframe,frames))
        show = Button(group,fg="red",bg="black",font=("gabriola",15,"bold"),text="Display",command=lambda: changeframe(showframe,frames,displaybox))
        # Placing buttons
        add.grid(row=0, column=0)
        delete.grid(row=0, column=1)
        show.grid(row=0, column=2)
        group.grid(row=0, column=0)

        changeframe(showframe,frames,displaybox)
