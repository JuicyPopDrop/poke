from pathlib import Path
import sqlite3
import pandas as pd
OUTPUT_PATH = Path(__file__).parent


class Datenbank:
    
    def erweiterung_existiert(self, Erweiterung):
        connection = sqlite3.connect("Datenbank/Sammlung.db")
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (Erweiterung,))
        result = cursor.fetchone()
        connection.close()
        return result is not None
    
    def addPokemonDB(Erweiterung, Nummer, Name, Typ, Zustand):
        connection = sqlite3.connect("Datenbank/Sammlung.db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO '{Erweiterung}' values({Nummer},'{Name}','{Typ}','{Zustand}')")
        connection.commit()
        connection.close()

    def addErweiterung(self, Erweiterung):
        connection = sqlite3.connect("Datenbank/Sammlung.db")
        cursor = connection.cursor()
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {Erweiterung} (Nummer INT, Name VARCHAR, Typ VARCHAR, Zustand VARCHAR)"
        )
        connection.commit()
        connection.close()
        
    def getErweiterungDB(self, Erweiterung):
        connection = sqlite3.connect("Datenbank/Sammlung.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (Erweiterung,)
        )
        result = cursor.fetchone()
        table_exists = result is not None
        if table_exists:
            print("Tabelle vorhanden")
        else:
            self.addErweiterung(Erweiterung)
        connection.close()


Erweiterungen = ["Test",
                "Maskerade im Zwielicht","Gewalten der Zeit","Paldeas Schicksale","Paradoxrift","151","Obisidianflammen","Entwicklungen in Paldea","Karmesin & Purpur",
                 "Zenit der Könige","Silberne Sturmwinde","Verlorener Ursprung","Pokemon Go","Astralglanz","Strahlende Sterne","Celebrations","Fusionsangriff","Drachenwandel","Schaurige Herrschaft","Kampfstile","Glänzendes Schicksal","Farbenschock","Weg des Champs","Flammende Finsternis","Clash der Rebellen","Schwert & Schild","Sonne & Mond","Stunde der Wächter","Nacht in Flammen","Schimmernde Legenden","Aufziehen der Sturmröte","McDonald's-Serie","Ultra-Prisma","Grauen der Lichtfinsternis","Sturm am Firmament","Majestät der Drachen","Echo des Donners","Teams sind Trumpf","Meisterdetektiv Pikachu","Kräfte im Einklang","Bund der Gleichgesinnten","Verborgenes Schicksal","Welten im Wandel",
                 "Willkommen in Kalos","Basisset","Flammenmeer","Fliegende Fäuste","Phantomkräfte","Protoschock","Double Crisis","Drachenleuchten","Ewiger Anfang","TURBOstart","TURBOfieber","Generationen","Schicksalsschmiede","Dampfkessel","Evolution",
                 "Schwarz & Weiß","Austreben der Mächtigen","Königliche Siege","Kommende Schicksale","Erforscher der Finsternis","Hoheit der Drachen","Dragon Vault","Überschrittene Schwellen","Plasma-Sturm","Plamsa-Frost","Plasma-Blaster","Legendary Treasures",
                 "HeartGold & HeartSilver","Entfesselt","Unerschrocken","Triumph","Ruf der Legenden",
                 "Platin","Aufstieg der Rivalen","Ultimative Sieger","Arceus",
                 "Diamant & Perl","Geheimnisvolle Schätze","Rätselhafte Wunder","Epische Begegnungen","Majestätischer Morgen","Erwachte Legenden","Sturmtief",
                 "EX Rubin & Saphir","EX Sandsturm","EX Drache","EX Team Magma vs. Team Aqua","EX Hidden Legends","EX Feuerrot und Blattgrün","EX Team Rocket Returns","EX Deoxys","EX Smaragd","EX Verborgene Mächte","EX Delta Species","EX Legend Maker","EX Holon Phantoms","EX Crystal Guardians","EX Dragon Frontiers","EX Power Keepers",
                 "Expedition","Aquapolis","Skyridge",
                 "Neo Genesis","Neo Entdeckung","Neo Revelation","Neo Destiny","Legendary Collection",
                 "Basis-Set","Dschungel","Fossil","Base Set 2","Team Rocket","Gym Heroes","Gym Challenge",
                 "Wizards Black Star Promos","Nintendo Black Star Promos","DP Black Star Promos","HGSS Black Star Promos","BW Black Star Promos","XY Black Star Promos","SM Black Star Promos","SWSH Black Star Promos","SV Blackstar Promos","Southern Island Collection","POP-Series","Pokemon Rumble","Meisterdetektiv Pickachu","Lets Play-Themendecks","25. Jubiläum-Kollektion","McDonald's Serie 2011","McDonald's Serie 2018","McDonald's Serie 2019","McDonald's Serie 2021","McDonald's Serie 2022","McDonald's Serie 2023"]

def addErweiterungen():
    connection = sqlite3.connect('Datenbank/Sammlung.db')
    cursor = connection.cursor()

    for erweiterung in Erweiterungen:
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS "{erweiterung}" (Nummer INT, Name VARCHAR, Typ VARCHAR, Zustand VARCHAR)""")

    connection.commit()
    connection.close()



def showTables():
    connection = sqlite3.connect('Datenbank/Sammlung.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Vorhandene Tabellen:")
    for table in tables:
        #print(table[0])
        continue

    connection.close()
    return(tables)

def kartenzeigen():
    conn = sqlite3.connect('deine_datenbank.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        if count > 0:
            print(table_name)
    conn.close()




def showfilledTables():
    conn = sqlite3.connect('Datenbank/Sammlung.db')
    cursor = conn.cursor()
    
    tables = []
    for x in showTables():
        cursor.execute(f"""SELECT * FROM "{x[0]}" """)
        table = cursor.fetchall()
        if table:
            tables.append([x[0],table])
    return tables
    
#conn = sqlite3.connect('Datenbank/Sammlung.db')
#cursor = conn.cursor()

#for x in showTables():
#   cursor.execute(f""" DROP TABLE "{x[0]}" """)   

     
