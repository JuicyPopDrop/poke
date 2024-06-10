import gui
import customtkinter as cTk
from PIL import Image

Gengar_Icon = ("Assets/gengar_icon.png")
                            

root = cTk.CTk()
root.title("Pokedex")
root.geometry("800x600")
root.resizable(width=0, height=0)
root.configure(background='#2a75bb')
root.iconbitmap(Gengar_Icon)

gui.main(root)

root.mainloop()