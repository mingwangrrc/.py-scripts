import sqlite3
import pandas as pd

data = pd.read_csv (r'example.csv')   
df = pd.DataFrame(data)

connection = sqlite3.connect('location.db')

crs = connection.cursor()

crs.execute("CREATE TABLE Hosts (host_id int NOT NULL PRIMARY KEY, ip_address varchar(15), mac_address varchar(14), manufacturer varchar(255))")

for row in df.itertuples():
  crs.execute('''
                INSERT INTO Hosts (host_id,ip_address, mac_address, manufacturer)
                VALUES (?,?,?,?)
                ''',(
                row.host_id,
                row.ip_address, 
                row.mac_address,
                row.manufacturer)
                )

connection.commit()
connection.close()

