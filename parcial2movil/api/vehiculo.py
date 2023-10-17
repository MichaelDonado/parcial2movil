from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vehiculo import Vehiculo, VehiculoSchema

route_vehiculos = Blueprint("route_vehiculos", __name__)

vehiculo_schema = VehiculoSchema()
vehiculos_schema = VehiculoSchema(many=True)

@route_vehiculos.route('/vehiculos', methods=['GET'])
def vehiculo():
    resultall = Vehiculo.query.all()
    result_vehiculos = vehiculos_schema.dump(resultall)
    return jsonify(result_vehiculos)

@route_vehiculos.route('/savevehiculo', methods=['POST'])
def save():
    placa = request.json['placa']
    modelo = request.json['modelo']
    capacidad = request.json['capacidad']
    new_vehiculo = Vehiculo(placa, modelo, capacidad)
    db.session.add(new_vehiculo)
    db.session.commit()
    return jsonify(vehiculos_schema.dump(new_vehiculo))



@route_vehiculos.route('/updatevehiculo', methods=['PUT'])
def Update():
    id = request.json['id']
    placa = request.json['placa']
    modelo = request.json['modelo']
    capacidad = request.json['capacidad']
    vehiculo = Vehiculo.query.get(id)
    if vehiculo:
        print(vehiculo)
        vehiculo.placa = placa
        vehiculo.modelo = modelo
        vehiculo.capacidad = capacidad
        db.session.commit()
        return jsonify(vehiculos_schema.dump(vehiculo))
    else:
        return "Error"

@route_vehiculos.route('/deletevehiculo/<id>', methods=['DELETE'])
def delete(id):
    vehiculo = Vehiculo.query.get(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return jsonify(vehiculo_schema.dump(vehiculo))