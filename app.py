from flask import Flask, jsonify,request
from base import base

app = Flask(__name__)
#Ruta raiz, que muestra el archivo base.py
@app.route("/")
def index():
    #Mostramo la base inicial sin dato
    return jsonify({"Base":base})

#Ruta de ingreso de datos para la creacion de usuario
@app.route("/createuser/", methods = ["POST"])
def input():
    #Variable que almacena los datos JSON enviados desde el formulario html
    new_user = {
        #Atibutos requeridos para la creacion del una usuario
        "name": request.json["name"],
        "email": request.json["email"],
        "password": request.json["password"],
        "addres": request.json["addres"],
        "phone": request.json["phone"],
        "date": request.json["date"]
    }
    #Agramos el nuevo usuario y sus datos a la base.py
    base.append(new_user)
    #Mostramos la base cargada de datos
    return jsonify({"Datos":base})

#Ruta para ingresar al sistema con autenticacion de usuario y contraseña
@app.route("/login/",methods =["POST"])
def login():
    #Variable que almacena los datos JSON enviados desde el formulario html
    consulta = {
        #Requisitos de autenticacion nombre y contraseña
        "name": request.json["name"],
        "password": request.json["password"]
    }
    #Recorido de la base para leer datos
    for u in base:
        #Lista que contendra los datos obtenidos a tratar
        buscarU = []
        #Condicional de validacion
        if u["name"] == consulta["name"] and u["password"] == consulta["password"]:
            #Agregamos el usuario referenciado a la lista
            buscarU.append(u)
     #Validamos que la lista contenga datos cargados       
    if(len(buscarU)>0):
        #Retornamos el ingreso exitoso
        return jsonify({"WELCOME":buscarU[0]["name"]})
    #Caso nulo de la validacion
    return jsonify({"ERROR":"USER INVALID"})

#Ruta de elininacion por condicional y metodo POST
@app.route("/delete/",methods = ["POST"])
def delete():
    
    consultar = {
        #Variable que almacena los datos JSON enviados desde el formulario html
        "name": request.json["name"],
        "password": request.json["password"]
    }
    #Recorido de la base para leer datos
    for u in base:
         #Lista que contendra los datos obtenidos a tratar
        buscarU = []
         #Condicional de validacion
        if u["name"] == consultar["name"] and u["password"] == consultar["password"]:
             #Agregamos el usuario referenciado a la lista
            buscarU.append(u)
            #Validamos que la lista contenga datos cargados  
    if(len(buscarU)>0):
        #Ejecutamos la eliminacion de datos cargados de base.py
        base.remove(buscarU[0])
        #Retornamos un mensaje exitoso
        return jsonify({"Mesaje":"Datos eliminados"})
    #Caso nulo de la validacion
    return jsonify({"ERROR":"DATOS INVALID"})

#Ruta de elininacion #2 por metodo http DELETE, sin datos de autenticacion.
@app.route("/delete/<string:name>", methods = ["DELETE"])
def eliminar(name):
    #Lista que contendra los datos obtenidos a tratar
    buscarU = []
    #Recorido de la base
    for u in base:
        #Validacion de usuario por http
        if u["name"]==name:
            #Agregamos el usuario en la lista
            buscarU.append(u)
    #Comparamos que la lista se encuentra cargada        
    if(len(buscarU)>0):
        #Eliminamos los datos obtenidos de la base.py
        base.remove(buscarU[0])
        #Imprimimos el caso exitoso
        return jsonify({"Mesaje":"Datos eliminados"})
    #Caso nulo de la validacion
    return jsonify({"ERROR":"DATOS INVALID"})
    
if __name__ == '__main__':
    app.run(debug = True, port = 5000)