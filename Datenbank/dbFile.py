from pathlib import Path
import sqlite3
import pandas as pd
OUTPUT_PATH = Path(__file__).parent


class Datenbank:
    def __init__(self, db_path):
        self.db_path = db_path

    def erweiterung_existiert(self, Erweiterung):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (Erweiterung,))
        result = cursor.fetchone()
        connection.close()
        return result is not None
    
    def addPokemonDB(self, Erweiterung, Nummer, Name, Typ, Zustand):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {Erweiterung} values({Nummer},{Name},{Typ},{Zustand}")
        connection.commit()
        connection.close()


    def addErweiterung(self, Erweiterung):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {Erweiterung} (Nummer INT, Name VARCHAR, Typ VARCHAR, Zustand VARCHAR)"
        )
        connection.commit()
        connection.close()
        
    def getErweiterungDB(self, Erweiterung):
        connection = sqlite3.connect(self.db_path)
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



    