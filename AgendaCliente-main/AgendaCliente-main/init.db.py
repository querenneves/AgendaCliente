import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO posts (title, emai, telefone, sexo, servico, data, horario, content) VALUES ('" + title + "', '" + email + "','" + telefone + "','" + sexo + "','" + servico + "','" + data + "','" + horario + "','" + content + "')")

connection.commit()
connection.close()