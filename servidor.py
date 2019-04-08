from flask import Flask, jsonify
app = Flask(__name__)

import mysql.connector

conexion = mysql.connector.connect(
    user = 'miguel',
    password = '12345',
    database = 'casas'
)

cursor = conexion.cursor()

@app.route("/api/v1/casas/")
def hello():
    query = "SELECT * FROM bienraiz"
    cursor.execute(query)
    #print(cursor.fetchall())
    casas = cursor.fetchall()
    lista_casas = []
    for casa in casas:
        c = {
            'id': casa[0],
            'titulo': casa[1],
            'precio': casa[2],
            'm2': casa[3],
            'rooms': casa[4],
            'baths': casa[5],
            'cars': casa[6],
            'description': casa[7]
        }
        lista_casas.append(c)
    return jsonify(lista_casas)

app.run()