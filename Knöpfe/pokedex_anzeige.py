import customtkinter


def pokedex_anzeigen():
    pokedex = customtkinter.CTk()
    pokedex.title("Deine Karten")
    pokedex.geometry("800x600")
    pokedex.resizable(width=0, height=0)
    pokedex.configure(background='#2a75bb')



    pokedex.mainloop()