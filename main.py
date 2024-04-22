import gui
import customtkinter

root = customtkinter.CTk()
root.title("Pokedex")
root.geometry("800x600")
root.resizable(width=0, height=0)
root.configure(background='#2a75bb')

gui.main(root)

root.mainloop()
