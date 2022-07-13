from tkinter import Button
from .Commonfunc import *
from .Database import update_data, get_data
from .patron import validate
from datetime import date

def status_tab(wd:list, txt:str):
    CANVAS, TUR_CNVS = wd[0]
    wd[3][3][3].config(text=txt) # Changing the text of status button
    forget(wd[1]) # Clearing screen
    CANVAS.itemconfig(wd[2], text='')
    forget(wd[3][1][1:]+wd[3][2][1:]+wd[3][3], lay_mngr="grid")  # Clearing children widgets
    unforget([wd[0][1], wd[3][0]],[(0.28, 0.06),(0.28, 0.2)]) # Placing required widgets
    unforget([wd[3][3][3]], [(2,1)], lay_mngr="grid")# Placing children widgets of frame

    if txt == 'ISSUE':
        unforget([ wd[3][1][1],wd[3][2][1] ], [(1,0),(1,1,4)], lay_mngr="grid")
    else:
        forget([ wd[3][1][1],wd[3][2][1] ],lay_mngr="grid")

    # Renaming labels
    wd[3][1][0].config(text=f"{'Book ID:': <10}")
    wd[3][1][1].config(text=f"{'Patron ID:': <10}")
    # Clearing entry widgets
    wd[3][2][0].delete(0,"end")
    wd[3][2][1].delete(0,"end")
    collapse(wd[4], wd[5])
    write_name(TUR_CNVS, txt)

def status(BOARD_WIDGETS:list,button:Button):
    BOOKID,PATRONID= BOARD_WIDGETS[2][0], BOARD_WIDGETS[2][1]
    bookid, patronid = BOOKID.get().strip().upper(), PATRONID.get().strip()
    data, txt  = get_data(),button['text']

    if bookid == "":
        msgbox("Please fill all details",0)
        return
    for rec in data:
        if rec[0] == bookid:
            BOOKID.delete(0,'end')
            PATRONID.delete(0,'end')
            # Returning a book
            if txt == 'RETURN':
                if rec[3].lower() == 'issued':
                    if msgbox(f"Return book: {rec[1]}",1):
                        update_data('status',"available",bookid)
                        update_data('patronid',None,bookid)
                        update_data('issuedate',None,bookid)
                        sound()
                else:
                    msgbox('Book is already available in library',0)

            # Issuing a book
            else:
                if patronid == "":
                    msgbox("Please fill all details",0)
                    return
                elif not patronid.isdigit():
                    msgbox(f'Invalid Patron ID: {patronid}.\nOnly numbers are accepted.',-1)
                    return
                elif len(patronid) >9:
                    msgbox(f'Invalid Patron ID: {patronid}.\nShould be less than 9 digits',-1)
                    return
                elif not validate(int(patronid),"primary"):
                    msgbox("Invalid Patron ID.",-1)
                    return
                elif rec[3].lower() == 'available':
                    if msgbox(f"Issue {rec[1]} to {validate(int(patronid),'name')}.",1):
                        update_data('status',"issued", bookid)
                        update_data('patronid',int(patronid),bookid)
                        update_data('issuedate',date.today(),bookid)
                        sound()
                else:
                    msgbox(f'Book is not available.\nAlready issued to {rec[4]}.',0)
                    return
            break
    else:   msgbox('Book Not Found\nPlease check book ID.',-1)
