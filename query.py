import sqlite3

connection = sqlite3.connect('location.db')

crs = connection.cursor()

# To enable a query remove the hashtag "#" from the beginning of the query statement. 
# If a database object is being created or updated the connection.commit() will also need to be uncommented.

# Selects all column data from the Hosts table
query = crs.execute("SELECT * FROM Hosts").fetchall()

# Selects only the ip_address column data from the Hosts table
#query = crs.execute("SELECT ip_address FROM Hosts").fetchall()

# Selects rows where the manufacturer name starts with Intel
#query = crs.execute("SELECT * FROM Hosts WHERE manufacturer LIKE 'Intel%'").fetchall()

# Inserts a new row into the Hosts table then commits the change
#query = crs.execute("INSERT INTO Hosts VALUES ('13','10.23.76.190','fbdd.f234.23ca','HP')").fetchall()
#connection.commit()

# Updates a row within the Hosts table where host_id (primary key) value equals 1 then commits the change
#query = crs.execute("UPDATE Hosts SET ip_address='1.1.1.1', mac_address='ffff.ffff.ffff', manufacturer='Xerox' WHERE host_id='1'").fetchall()
#connection.commit()

# Deletes a row from the Hosts table where the host_id value equals 13 then commits the change
#query = crs.execute("DELETE FROM Hosts WHERE host_id='13'").fetchall()
#connection.commit()

print(query)

connection.close()

