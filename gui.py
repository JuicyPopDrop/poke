import tkinter as tk
from tkinter import *
from Assets.Font import *
from Assets import *
from PIL import Image, ImageTk



root = tk.Tk()
root.title("Pokedex")
root.geometry("800x600")
root.resizable(width=0, height=0)
root.configure(background='#2a75bb')

unterordner = "Assets"
unterordner2 = "Buttons"
unterordner3 = "Typ_Buttons"

blanko_karte_dateiname = "blanko_karte.png"
Typ_Psycho_dateiname = "Typ_Psycho.png"

blanko_karte = Image.open(f"{unterordner}/{blanko_karte_dateiname}")
tk_blanko_karte = ImageTk.PhotoImage(blanko_karte)

Typ_Psycho = Image.open(f"{unterordner}/{unterordner2}/{unterordner3}/{Typ_Psycho_dateiname}")
tk_Typ_Psycho = ImageTk.PhotoImage(Typ_Psycho)

labelÜberschrift = Label(master=root, justify=CENTER, text="Pokedex",
                         fg="#ffcb05", bg="#2a75bb", font=("Pokemon Solid", 20))
labelÜberschrift.place(x=340, y=20, width=120, height=50)


labelKarte = Label(master=root, image = tk_blanko_karte, bg="#2a75bb")
labelKarte.place(x=277, y=160, width=245, height=342)

labelTyp = Label(master=root, image = tk_Typ_Psycho)
labelTyp.place(x= 500, y=160, width = 20, height= 20)

root.mainloop()
