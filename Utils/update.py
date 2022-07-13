from .Commonfunc import *
from .patron import validate
from .Database import get_data, update_data


def update_tab(wd: list):
    CANVAS, TUR_CNVS = wd[0]
    forget(wd[1]) # Clearing screen
    forget(wd[3][1][1:]+wd[3][2][1:]+wd[3][3],lay_mngr="grid")  # Clearing children widgets
    unforget([wd[0][1], wd[3][0]],[(0.26, 0.06),(0.26, 0.2)]) # Placing required widgets
    CANVAS.itemconfig(wd[2], text='')
    unforget(wd[3][1][1:3]+wd[3][2][2:4]+[wd[3][3][2]], [(1,0),(2,0),(2,1,4),(1,1),(3,1)], lay_mngr="grid")# Placing required children widgets
    # Renaming labels
    wd[3][1][0].config(text=f"{'Current Book ID:': <16}")
    wd[3][1][1].config(text=f"{'Choose field:': <16}")
    wd[3][1][2].config(text=f"{'New Data:': <16}")
    # Clearing entry widgets
    wd[3][2][0].delete(0,"end")
    wd[3][2][1].delete(0,"end")
    wd[3][2][2].delete(0,"end")
    collapse(wd[4], wd[5])
    write_name(TUR_CNVS, "UPDATE")

def update(BOARD_WIDGETS:list, item: StringVar):
    currentid = BOARD_WIDGETS[2][0].get().strip()
    field = item.get().strip()
    newdata = BOARD_WIDGETS[2][2].get().strip().title()
    data = get_data()
    FIELD = {'Book ID':('BookID',0), 'Book Name':('BookName',1), 'Author Name':('Author',2), 'Patron ID':('PatronID',4), 'Issue Date':('IssueDate',5) }
    # Checking for invalid entry
    found = False
    if currentid == "" or newdata == "":
        msgbox("Please fill all details",0)
        return
    for r in data:
        if field == "Book ID":
            if r[0].lower() == newdata.lower(): # If bookid alredy exists
                msgbox(f"Book ID '{newdata.upper()}' already exists!",-1)
                return
    for r in data:
        if r[0].lower() == currentid.lower():
            if field == "--Select--":
                msgbox("Please select a field name.", 0)
                return
            elif field == 'Patron ID':
                if not newdata.isdigit():
                    msgbox("Please enter a valid ID.\nOnly numbers are accepted", -1)
                    return
                elif r[3] == 'available':
                    msgbox("Book is not issued.\nPatron ID can only be change with issued books", -1)
                    return
                elif not validate(int(newdata),"primary"):
                    msgbox("Invalid Patron ID.",-1)
                    return
            current_data = r[FIELD[field][1]]
            found = True
            break
    if found:
        try:
            if msgbox(f"Current {field}: {current_data}\nNew {field}: {newdata}\n\nDo you want to update?",1):
                # Clearing entry box
                BOARD_WIDGETS[2][0].delete(0,'end')
                BOARD_WIDGETS[2][2].delete(0,"end")
                BOARD_WIDGETS[2][0].update()
                BOARD_WIDGETS[2][2].update()
                item.set("--Select--")
                update_data(FIELD[field][0],newdata,currentid)
                sound()
        except Exception:
            msgbox(f"Data too long.\nExceeds maximum limit.",-1)
    else:
        msgbox("Book Record Not Found\nPlease check book ID.",-1)
