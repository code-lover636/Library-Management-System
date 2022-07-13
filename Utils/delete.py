from .Commonfunc import *
from .Database import del_data, get_data


def delete_tab(wd:list):
    CANVAS, TUR_CNVS = wd[0]
    forget(wd[1])# Clearing screen
    forget(wd[3][1][1:]+wd[3][2][1:]+wd[3][3], lay_mngr="grid") # Clearing children widgets
    CANVAS.itemconfig(wd[2], text='')
    unforget([wd[3][0], wd[0][1]], [(0.28, 0.2), (0.28, 0.06)]) # Placing required widgets
    unforget([wd[3][3][1]], [(1,1)], lay_mngr="grid") # Placing children widgets
    # Renaming labels
    wd[3][1][0].config(text="Book ID:")
    # Clearing entry widgets
    wd[3][2][0].delete(0,"end")
    # Collapsing sidebar
    collapse(wd[4], wd[5])
    write_name(TUR_CNVS, "DELETE")
    


def delete(BOARD_WIDGETS:list):
    BOOKID = BOARD_WIDGETS[2][0]
    bid = BOOKID.get().strip()
    data = get_data()

    if bid != '':
        for rec in data:
            if bid.lower() == rec[0].lower():
                if msgbox(f"Are you sure you want to delete the book\n'{rec[1]}'?",1):
                    del_data(bid)
                    BOOKID.delete(0, 'end')
                    BOOKID.update()
                    sound()
                break
        else:   msgbox('Book Not Found\nPlease check book ID.',-1)
    else:   msgbox('Please enter a Book ID',0)
