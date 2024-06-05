import customtkinter as cTk
from CTkListbox import * 
from Datenbank import dbFile

def pokedex_anzeigen():
    pokedex = cTk.CTk()
    pokedex.title("Deine Karten")
    pokedex.geometry("800x600")
    pokedex.resizable(width=0, height=0)
    pokedex.configure(background='#2a75bb')
    
    Erweiterungen = dbFile.showfilledTables()
    count = 0

    listbox = CTkListbox(pokedex,
                         width = 400, height = 600,
                         command = 0)
    listbox.place(x = 0, y = 0)
    
    for x in Erweiterungen:
        listbox.insert(count, x[0])
        count += 1

    
    
    
    
    
    
    
    
    
    
    pokedex.mainloop()

