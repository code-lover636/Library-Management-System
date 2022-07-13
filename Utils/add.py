from .Commonfunc import *
from .Database import add_data, get_data


def add_tab(wd:list):
    CANVAS, TUR_CNVS = wd[0]
    forget(wd[1]) # Clearing screen
    forget(wd[3][1][1:]+wd[3][2][1:]+wd[3][3], lay_mngr="grid") # Clearing children widgets
    CANVAS.itemconfig(wd[2], text='')
    unforget([wd[3][0], wd[0][1]], [(0.28, 0.2), (0.28, 0.06)]) # Placing required widgets
    unforget(wd[3][1][1:3]+wd[3][2][1:3]+[wd[3][3][0]], [(1,0),(2,0),(1,1,4),(2,1,4),(3,1)], lay_mngr="grid") # Placing children widgets
    # Renaming labels
    wd[3][1][0].config(text=f"{'Book ID:': <10}")
    wd[3][1][1].config(text=f"{'Book Name:': <10}")
    wd[3][1][2].config(text=f"{'Author:': <10}")
    # Clearing entry widgets
    wd[3][2][0].delete(0,"end")
    wd[3][2][1].delete(0,"end")
    wd[3][2][2].delete(0,"end")
    collapse(wd[4], wd[5])
    write_name(TUR_CNVS, "+ADD BOOK")
    

def add(BOARD_WIDGETS:list):
    BOOKID, BOOKNAME, ATHRNAME = BOARD_WIDGETS[2][0:3]
    data = get_data()
    bid, bname, athr = BOOKID.get().strip(), BOOKNAME.get().strip(), ATHRNAME.get().strip()
    
    if bid == "" or bname == "" or athr == "":  msgbox("Please fill all details",0)
    else:
        for rec in data:
            if bid.upper() == rec[0].upper():
                msgbox(f"Book ID '{bid}' already exists!",0)
                break
        else:
            if len(bid)>10 or len(bname)>100 or len(athr)>70:
                msgbox(f"Data too long.\nExceeds maximum limit.",-1)
            elif msgbox(f"Add book: {bname} to book list",1): 
                add_data(bid.upper(), bname.title(), athr.title())
                BOOKID.delete(0, "end")
                BOOKNAME.delete(0, "end")
                ATHRNAME.delete(0, "end")
                BOOKID.update()
                BOOKNAME.update()
                ATHRNAME.update()
                sound()
