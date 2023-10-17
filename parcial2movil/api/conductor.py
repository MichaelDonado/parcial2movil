from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.conductor import Conductor, ConductorSchema

route_conductores = Blueprint("route_conductores", __name__)

conductor_schema = ConductorSchema()
conductores_schema = ConductorSchema(many=True)

@route_conductores.route('/conductores', methods=['GET'])
def conductor():
    resultall = Conductor.query.all()
    result_conductor = conductor_schema.dump(resultall)
    return jsonify(result_conductor)

@route_conductores.route('/saveconductor', methods=['POST'])
def save():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    telefono = request.json['telefono']
    licencia = request.json['licencia']

    new_conductor = Conductor(nombre, apellido, telefono, licencia)
    db.session.add(new_conductor)
    db.session.commit()
    return jsonify(conductor_schema.dump(new_conductor))

@route_conductores.route('/updateconductor', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    telefono = request.json['telefono']
    licencia = request.json['licencia']
    
    conductor = Conductor.query.get(id)
    if conductor:
        print(conductor)
        conductor.nombre = nombre
        conductor.apellido = apellido
        conductor.telefono = telefono
        conductor.licencia = licencia
        db.session.commit()
        return jsonify(conductor_schema.dump(conductor))
    else:
        return "Error"

@route_conductores.route('/deleteconductor/<id>', methods=['DELETE'])
def delete(id):
    conductor = Conductor.query.get(id)
    db.session.delete(conductor)
    db.session.commit()
    return jsonify(conductor_schema.dump(conductor))