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


Erweiterungen = []

def addErweiterungen():
    connection = sqlite3.connect('Datenbank/Sammlung.db')
    cursor = connection.cursor()

    for erweiterung in Erweiterungen:
        if any(char in erweiterung for char in ['&', '-', ' ', '!']):
            tabellenname = f'"{erweiterung}"'
        else:
            tabellenname = erweiterung.replace(' ', '_')                
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {tabellenname} (Nummer INT, Name VARCHAR, Typ VARCHAR, Zustand VARCHAR)")

    connection.commit()
    connection.close()



def showTables():
    connection = sqlite3.connect('Datenbank/Sammlung.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Vorhandene Tabellen:")
    for table in tables:
        print(table[0])

    connection.close()

   




    