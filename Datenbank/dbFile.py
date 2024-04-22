from pathlib import Path
import sqlite3
import pandas as pd
OUTPUT_PATH = Path(__file__).parent




def addPokemonDB(Erweiterung,Nummer,Name,Typ,Condition):
    connection = sqlite3.connect(OUTPUT_PATH / "Sammlung.db")
    cursor = connection.cursor()
    cursor.execute(
        f"Insert into {Erweiterung} values('{Nummer}','{Name}','{Typ}','{Condition}')"
    )
    connection.commit()

def addErweiterungDB(Erweiterung):
    connection = sqlite3.connect(OUTPUT_PATH / "Sammlung.db")
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE {Erweiterung}(Nummer INT,
                                                Name VARCHAR,
                                                Typ VARCHAR,
                                                Condition VARCHAR)"

    )
    return connection.commit()

def getErweiterungDB(Erweiterung):
    connection = sqlite3.connect(OUTPUT_PATH / "Sammlung.db")
    cursor = connection.cursor()
    table_name = "ausgewählte Erweiterung"
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()
    table_exists = any(table[0] == table_name for table in tables)

    if table_exists:
        print("Table vorhanden")
    else:
        addErweiterungDB()

    