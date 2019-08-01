# CREATE TABLE countries (
#     code       VARCHAR (3)  PRIMARY KEY,
#     name       VARCHAR (50),
#     population NUMBER (10),
#     area       NUMBER (10) 
# );

import sqlite3
import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
con = sqlite3.connect(r"e:\classroom\python\june24\training.db")
cur = con.cursor()

for country in countries:
    print("Loading ", country['name'])
    cur.execute("insert into countries values(?,?,?,?)",
                ( country['alpha3Code'],country['name'], country['population'], country['area']))

con.commit()
cur.close()
con.close()
