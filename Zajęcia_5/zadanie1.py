import sqlite3

# Połączenie z plikiem bazy danych (utworzy plik sales.db, jeśli nie istnieje)
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

#Zadanie 1a)
print ("--------------------------ZADANIE 1A------------------------------")
cursor.execute("SELECT * FROM sales WHERE product = 'Laptop'")
rows = cursor.fetchall()
for row in rows:
    print(row)

#Zadanie 1b)
print ("--------------------------ZADANIE 1B------------------------------")
cursor.execute("SELECT * FROM sales WHERE date IN ('2025-05-07','2025-05-08')")

rows = cursor.fetchall()
for row in rows:
    print(row)

#Zadanie 1c)
print ("--------------------------ZADANIE 1C------------------------------")
cursor.execute("SELECT * FROM sales WHERE price > 200")

rows = cursor.fetchall()
for row in rows:
    print(row)

#Zadanie 1d)
print ("--------------------------ZADANIE 1C------------------------------")
cursor.execute("SELECT id,product, price*quantity FROM sales")

rows = cursor.fetchall()
for row in rows:
    print(row)


#Zadanie 1e)
print ("--------------------------ZADANIE 1E------------------------------")
cursor.execute("SELECT COUNT(*) as x, MAX(*) as m ,date FROM sales GROUP BY date ORDER BY x DESC LIMIT 1 ")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


