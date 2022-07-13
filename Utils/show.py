from .Commonfunc import *
from .Database import get_data


def show(wd:list):
    # Required widgets
    CANVAS, TUR_CNVS = wd[0]    
    DISPLAY = wd[1][1]
    # Writing field names into listbox
    DISPLAY.delete(0, "end")        
    DISPLAY.insert(0, f"{'BOOK ID':<10}{'BOOK NAME':<50}{'AUTHOR':<25}{'STATUS':<15}{'PATRON ID': <15}{'ISSUE DATE'}")
    DISPLAY.itemconfig(0, {"fg":"red", "bg":"black"})
    # Writing data from database 
    table = get_data()  # List of nested tuples
    for rec in table:
        rec=list(rec)
        if rec[4] == rec[5]==None:
            rec[4] = "----"
            date = "----------"
        else:
            date = str(rec[5]).split('-')
            date = date[2]+"-"+date[1]+"-"+date[0]
        
        if   len(rec[0]) > 9 : rec[0] = rec[0][:6] +"..."
        elif len(rec[1]) > 49: rec[1] = rec[1][:46]+"..."
        elif len(rec[2]) > 24: rec[2] = rec[2][:21]+"..."
        elif len(rec[3]) > 14: rec[3] = rec[0][:11]+"..."
        elif len(str(rec[4])) > 14: rec[0] = rec[0][:11]+"..."
        
        DISPLAY.insert("end", f"{rec[0]:<10}{rec[1]:<50}{rec[2]:<25}{rec[3]:<15}{rec[4]: <15}{date}")
    # Clearing screen and placing required widgets
    forget([wd[3][0]])
    CANVAS.itemconfig(wd[2], text="")
    unforget(wd[1]+[wd[0][1]], [(0.4,0.12), (0.17, 0.2), (0.17, 0.06)])
    collapse(wd[4], wd[5]) 
    write_name(TUR_CNVS, "BOOK LIST")


def search(DISPLAY: Listbox, search_entry: Entry):
    query = search_entry.get().strip()
    data = get_data() # List of nested tuples
    
    # Searching through data with a keyword as query
    if query != "":
        DISPLAY.delete(0, "end")
        # Writing back field names
        DISPLAY.insert(0, f"{'BOOK ID':<10}{'BOOK NAME':<50}{'AUTHOR':<25}{'STATUS':<15}{'PATRON ID': <15}{'ISSUE DATE'}")
        DISPLAY.itemconfig(0, {'fg':'red', 'bg':'black'})
        # Writing matching records
        for rec in data:
            rec=list(rec)
            if query.lower() == rec[0].lower() or query.lower() in rec[1].lower() or query.lower() in rec[2].lower()\
            or query.lower() == rec[3].lower() or query.lower() == str(rec[4]) or query.lower() in str(rec[5]) :
                if rec[4] == rec[5]==None:
                    rec[4] = '----'
                    date = '----------'
                else:
                    date = str(rec[5]).split('-')
                    date = date[2]+'-'+date[1]+'-'+date[0]
                
                if   len(rec[0]) > 9 : rec[0] = rec[0][:6] +"..."
                elif len(rec[1]) > 49: rec[1] = rec[1][:46]+"..."
                elif len(rec[2]) > 24: rec[2] = rec[2][:21]+"..."
                elif len(rec[3]) > 14: rec[3] = rec[0][:11]+"..."
                elif len(str(rec[4])) > 14: rec[0] = rec[0][:11]+"..."
                
                DISPLAY.insert("end",f"{rec[0][:9]:<10}{rec[1][:49]:<50}{rec[2][:24]:<25}{rec[3]:<15}{rec[4]: <15}{date}")
        # Message for no matching results   
        if DISPLAY.size()==1:
            DISPLAY.delete(0, "end")
            DISPLAY.insert(0,"")
            DISPLAY.insert(1, '%sNO MATCHING RESULTS FOR \"%s\"'%(" "*50, query))
