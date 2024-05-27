import customtkinter as cTk
from CTkListbox import * 
from PIL import Image
from Datenbank import dbFile
from tkinter.messagebox import showinfo, showerror
from CTkListbox import *

Typen = ["Typen",
        "Normal","Feuer","Wasser","Elektro","Pflanze",
         "Flug","Käfer","Gift","Gestein","Boden",
         "Kampf","Eis","Psycho","Geist","Drache",
         "Unlicht","Stahl","Fee",]

Erweiterungen = ["Erweiterung wählen",
                 "---Karmesin & Purpur---",
                 "Maskerade im Zwielicht","Gewalten der Zeit","Paldeas Schicksale","Paradoxrift","151","Obisidianflammen","Entwicklungen in Paldea","Karmesin & Purpur",
                 "---Schwert & Schild---",
                 "Zenit der Könige","Silberne Sturmwinde","Verlorener Ursprung","Pokemon Go","Astralglanz","Strahlende Sterne","Celebrations","Fusionsangriff","Drachenwandel","Schaurige Herrschaft","Kampfstile","Glänzendes Schicksal","Farbenschock","Weg des Champs","Flammende Finsternis","Clash der Rebellen","Schwert & Schild",
                 "---Sonne & Mond---",
                 "Sonne & Mond","Stunde der Wächter","Nacht in Flammen","Schimmernde Legenden","Aufziehen der Sturmröte","McDonald's-Serie","Ultra-Prisma","Grauen der Lichtfinsternis","Sturm am Firmament","Majestät der Drachen","Echo des Donners","Teams sind Trumpf","Meisterdetektiv Pikachu","Kräfte im Einklang","Bund der Gleichgesinnten","Verborgenes Schicksal","Welten im Wandel",
                 "---XY---",
                 "Willkommen in Kalos","Basisset","Flammenmeer","Fliegende Fäuste","Phantomkräfte","Protoschock","Double Crisis","Drachenleuchten","Ewiger Anfang","TURBOstart","TURBOfieber","Generationen","Schicksalsschmiede","Dampfkessel","Evolution",
                 "---Schwarz & Weiß---",
                 "Schwarz & Weiß","Austreben der Mächtigen","Königliche Siege","Kommende Schicksale","Erforscher der Finsternis","Hoheit der Drachen","Dragon Vault","Überschrittene Schwellen","Plasma-Sturm","Plamsa-Frost","Plasma-Blaster","Legendary Treasures",
                 "---HeartGold & HeartSilver---",
                 "HeartGold & HeartSilver","Entfesselt","Unerschrocken","Triumph","Ruf der Legenden",
                 "---Platin---",
                 "Platin","Aufstieg der Rivalen","Ultimative Sieger","Arceus",
                 "---Diamant & Perl---",
                 "Diamant & Perl","Geheimnisvolle Schätze","Rätselhafte Wunder","Epische Begegnungen","Majestätischer Morgen","Erwachte Legenden","Sturmtief",
                 "---EX---",
                 "EX Rubin & Saphir","EX Sandsturm","EX Drache","EX Team Magma vs. Team Aqua","EX Hidden Legends","EX Feuerrot und Blattgrün","EX Team Rocket Returns","EX Deoxys","EX Smaragd","EX Verborgene Mächte","EX Delta Species","EX Legend Maker","EX Holon Phantoms","EX Crystal Guardians","EX Dragon Frontiers","EX Power Keepers",
                 "---e-Card-Serie---",
                 "Expedition","Aquapolis","Skyridge",
                 "---Neo-Serie---",
                 "Neo Genesis","Neo Entdeckung","Neo Revelation","Neo Destiny","Legendary Collection",
                 "---Basis-Serie---",
                 "Basis-Set","Dschungel","Fossil","Base Set 2","Team Rocket","Gym Heroes","Gym Challenge",
                 "---Promos und Specials---",
                 "Wizards Black Star Promos","Nintendo Black Star Promos","DP Black Star Promos","HGSS Black Star Promos","BW Black Star Promos","XY Black Star Promos","SM Black Star Promos","SWSH Black Star Promos","SV Blackstar Promos","Southern Island Collection","POP-Series","Pokemon Rumble","Meisterdetektiv Pickachu","Lets Play-Themendecks","25. Jubiläum-Kollektion","McDonald's Serie 2011","McDonald's Serie 2018","McDonald's Serie 2019","McDonald's Serie 2021","McDonald's Serie 2022","McDonald's Serie 2023"]

def main(canvas, dbFile):  
    
    def addPokemon(Name, Nummer, Typ, Erweiterung):
        if Name and Nummer and Typ and Erweiterung:

            bestätigung = f"Du fügst hinzu:\nName: {Name}\nNummer: {Nummer}\nTyp: {Typ}\nErweiterung: {Erweiterung}"

            showinfo("Bestätigung", bestätigung)

            Zustand = ""
            if NonHoloCheck_var.get() == "on":
                Zustand += "Non Holo, "
            if ReverseHoloCheck_var.get() == "on":
                Zustand += "Reverse Holo, "
            if HoloCheck_var.get() == "on":
                Zustand += "Holo, "
            if GoldCheck_var.get() == "on":
                Zustand += "Gold, "
            if RainbowCheck_var.get() == "on":
                Zustand += "Rainbow, "

            Zustand = Zustand.rstrip(", ")

            dbFile.Datenbank.addPokemonDB(Erweiterung, Nummer, Name, Typ, Zustand)

            showinfo("Erfolg", "Das Pokémon wurde erfolgreich hinzugefügt!")
        else:
            showerror("Fehler", "Bitte fülle alle Felder aus!")


    my_image = cTk.CTkImage(dark_image=Image.open("Assets/blanko_karte.png"),
                            size = (800,600))

    blankoKarte = cTk.CTkLabel(canvas, image = my_image,
                               fg_color="#2a75bb")
    blankoKarte.place(x=0, y=0)
    
    Überschrift = cTk.CTkLabel(canvas, text="Pokedex",
                                        fg_color="#2a75bb", text_color="#ffcb05", 
                                        font=("Pokemon Solid", 20),
                                        width=120, height=60)
    Überschrift.place(x=340, y=20) 

    NameEntry = cTk.CTkEntry(canvas, height = 20, width = 100, placeholder_text="Name")
    NameEntry.place(x=340,y=140)

    TypListe = cTk.CTkOptionMenu(canvas, values = Typen, 
                                 height = 20, width = 65,corner_radius = 0, 
                                 bg_color = "#343638", fg_color = "#343638",
                                 button_color = "#343638", button_hover_color = "#3c5aa6",
                                 )
    TypListe.place(x=445,y=140)

    ErweiterungListe = cTk.CTkOptionMenu(canvas, values = Erweiterungen,
                                         height = 20, width = 100,corner_radius = 0,
                                         bg_color = "#343638", fg_color = "#343638",
                                         button_color = "#343638", button_hover_color = "#3c5aa6",
    )
    ErweiterungListe.place(x=530,y=140)


    NummerEntry = cTk.CTkEntry(canvas, height = 20, width = 65, placeholder_text="Nummer")
    NummerEntry.place(x=290,y=440)


    NonHoloCheck_var = cTk.StringVar(value="off")
    NonHolo_var = cTk.StringVar(value="Non Holo")
    NHCheck = cTk.CTkCheckBox(canvas, text = "Non Holo",
                              variable = NonHoloCheck_var, onvalue="on", offvalue = "off",
                              checkbox_width = 20,
                              checkbox_height = 20,
                              font = ("Helvetica",10),
                              corner_radius = 5,
                              fg_color ="#3c5aa6",
                              bg_color = "#2a75bb",
                              hover_color = "green",
                              text_color = "#ffcb05",
                              hover=False,
                              textvariable = NonHolo_var,
                              )
    NHCheck.place(x=230, y=480)

    ReverseHoloCheck_var = cTk.StringVar(value="off")
    ReverseHolo_var = cTk.StringVar(value="Reverse Holo")
    ReverseCheck = cTk.CTkCheckBox(canvas, text = "Reverse Holo",
                              variable = ReverseHoloCheck_var, onvalue="on", offvalue = "off",
                              checkbox_width = 20,
                              checkbox_height = 20,
                              font = ("Helvetica",10),
                              corner_radius = 5,
                              fg_color ="#3c5aa6",
                              bg_color = "#2a75bb",
                              hover_color = "green",
                              text_color = "#ffcb05",
                              hover=False,
                              textvariable = ReverseHolo_var,
                              )
    ReverseCheck.place(x=305, y=480)

    HoloCheck_var = cTk.StringVar(value="off")
    Holo_var = cTk.StringVar(value=" Holo")
    HoloCheck = cTk.CTkCheckBox(canvas, text = " Holo",
                              variable = HoloCheck_var, onvalue="on", offvalue = "off",
                              checkbox_width = 20,
                              checkbox_height = 20,
                              font = ("Helvetica",10),
                              corner_radius = 5,
                              fg_color ="#3c5aa6",
                              bg_color = "#2a75bb",
                              hover_color = "green",
                              text_color = "#ffcb05",
                              hover=False,
                              textvariable = Holo_var,
                              )
    HoloCheck.place(x=400, y=480)

    GoldCheck_var = cTk.StringVar(value="off")
    Gold_var = cTk.StringVar(value=" Gold")
    GoldCheck = cTk.CTkCheckBox(canvas, text = " Gold",
                              variable = GoldCheck_var, onvalue="on", offvalue = "off",
                              checkbox_width = 20,
                              checkbox_height = 20,
                              font = ("Helvetica",10),
                              corner_radius = 5,
                              fg_color ="#3c5aa6",
                              bg_color = "#2a75bb",
                              hover_color = "green",
                              text_color = "#ffcb05",
                              hover=False,
                              textvariable = Gold_var,
                              )
    GoldCheck.place(x=460, y=480)

    RainbowCheck_var = cTk.StringVar(value="off")
    Rainbow_var = cTk.StringVar(value=" Rainbow")
    RainbowCheck = cTk.CTkCheckBox(canvas, text = " Rainbow",
                              variable = RainbowCheck_var, onvalue="on", offvalue = "off",
                              checkbox_width = 20,
                              checkbox_height = 20,
                              font = ("Helvetica",10),
                              corner_radius = 5,
                              fg_color ="#3c5aa6",
                              bg_color = "#2a75bb",
                              hover_color = "green",
                              text_color = "#ffcb05",
                              hover=False,
                              textvariable = Rainbow_var,
                              )
    RainbowCheck.place(x=520, y=480)
    
    HinzufügenButton = cTk.CTkButton(canvas,text="Hinzufügen",corner_radius=5,
                                     height=40,width=150,fg_color="#3c5aa6",bg_color="#2a75bb",
                                     command=lambda: addPokemon(NameEntry.get(),
                                                                NummerEntry.get(),
                                                                TypListe.get(),
                                                                ErweiterungListe.get()),)
    HinzufügenButton.place(x=325,y=510)

    

    
    