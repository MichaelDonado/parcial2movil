from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.ciudad import Ciudad, CiudadSchema

route_ciudades = Blueprint("route_ciudades", __name__)

ciudad_schema = CiudadSchema()
ciudades_schema = CiudadSchema(many=True)


@route_ciudades.route("/ciudades", methods=["GET"])
def Ciudad():
    resultall = Ciudad.query.all()  
    resultado_ciudad = ciudades_schema.dump(resultall)
    return jsonify(resultado_ciudad)


@route_ciudades.route("/saveciudad", methods=["POST"])
def save():
    nombre = request.json['nombre']
    departamento = request.json['departamento']
    origen = request.json['origen']
    destino = request.json['destino']
    new_ciudad = Ciudad(nombre, departamento, origen, destino)
    db.session.add(new_ciudad)
    db.session.commit()
    return jsonify(ciudad_schema.dump(new_ciudad))


@route_ciudades.route("/updateciudad", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json['nombre']
    departamento = request.json['departamento']
    origen = request.json['origen']
    destino = request.json['destino']
    ciudad = Ciudad.query.get(id)
    if ciudad:
        print(ciudad)
        ciudad.nombre = nombre
        ciudad.departamento = departamento
        ciudad.origen = origen
        ciudad.destino = destino
        db.session.commit()
        return jsonify(ciudad_schema.dump(ciudad))
    else:
        return "Error"


@route_ciudades.route("/deleteciudad/<id>", methods=["DELETE"])
def eliminar(id):
    ciudad = Ciudad.query.get(id)
    db.session.delete(ciudad)
    db.session.commit()
    return jsonify(ciudad_schema.dump(ciudad))
