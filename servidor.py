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
    query2 = "select colonia.nombre, municipio.nombre from bienraiz left join colonia on colonia.id = bienraiz.id_colonia " \
            "left join municipio on municipio.id = colonia.id_municipio where bienraiz.id = %s"
    query3 = "select imagen.ubicacion from bienraiz left join imagen on imagen.id_bienraiz = bienraiz.id where bienraiz.id = %s"
    for casa in casas:
        cursor.execute(query2, (casa[0],))
        ubicacion = cursor.fetchall()
        colonia = ubicacion[0][0]
        municipio = ubicacion[0][1]

        cursor.execute(query3, (casa[0],))
        i = cursor.fetchall()

        c = {
            'id': casa[0],
            'titulo': casa[1],
            'precio': casa[2],
            'm2': casa[3],
            'rooms': casa[4],
            'baths': casa[5],
            'cars': casa[6],
            'description': casa[7],
            'colonia': colonia,
            'municipio': municipio,
            'imgs': i
        }
        lista_casas.append(c)
    all = {
        'casas': lista_casas
    }
    return jsonify(all)

app.run()