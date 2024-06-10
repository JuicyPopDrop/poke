import customtkinter as cTk
from CTkListbox import *
from Datenbank import dbFile

def pokedex_anzeigen():
    # Hauptfenster für den Pokedex
    pokedex = cTk.CTk()
    pokedex.title("Deine Karten")
    pokedex.geometry("800x600")
    pokedex.resizable(width=0, height=0)
    pokedex.configure(background='#2a75bb')
    
    # Abfrage der gefüllten Tabellen aus der Datenbank
    Erweiterungen = dbFile.showfilledTables()
    count = 0

    # Listbox für die Anzeige der Tabellen
    Erweiterungsliste = CTkListbox(pokedex,
                                   width=400, height=600,
                                   command=lambda x: ErweiterungAuswahl(x))
    Erweiterungsliste.place(x=0, y=0)
    
    for x in Erweiterungen:
        Erweiterungsliste.insert(count, x[0])
        count += 1

    # Funktion zur Auswahl einer Erweiterung und Anzeige der Karten
    def ErweiterungAuswahl(gewählte_erweiterung):
        # Vorherige Kartenliste löschen
        for widget in pokedex.winfo_children():
            if isinstance(widget, CTkListbox) and widget != Erweiterungsliste:
                widget.destroy()
        
        # Abfrage der Karten aus der ausgewählten Erweiterung
        Karten = dbFile.getCardsFromTable(gewählte_erweiterung)
        
        # Listbox für die Anzeige der Karten
        Kartenliste = CTkListbox(pokedex,
                                 width=400, height=600,
                                 command=0)
        Kartenliste.place(x=400, y=0)
        
        for count, karte in enumerate(Karten):
            # Kombinierte Anzeige aller Karteninformationen
            karte_info = " | ".join(str(info) for info in karte)
            Kartenliste.insert(count, karte_info)

    pokedex.mainloop()
