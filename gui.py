import customtkinter as cTk
from Knöpfe import buttons
from tkinter import Tk, Frame, Canvas, Entry, Text, Button, PhotoImage

def main(root):
    
    canvas = Canvas(
        root,
        bg="#2a75bb",
        height=900,
        width=1600,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    
    db = None

    buttons.main(root,db)

    
