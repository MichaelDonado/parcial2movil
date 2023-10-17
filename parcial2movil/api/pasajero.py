from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pasajero import Pasajero, PasajeroSchema

route_pasajeros = Blueprint("route_pasajeros", __name__)

pasajero_schema = PasajeroSchema()
pasajeros_schema = PasajeroSchema(many=True)

@route_pasajeros.route('/pasajeros', methods=['GET'])
def pasajero():
    resultall = Pasajero.query.all()
    result_pasajero = pasajeros_schema.dump(resultall)
    return jsonify(result_pasajero)

@route_pasajeros.route('/savepasajero', methods=['POST'])
def save():
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    email = request.json['email']
    num_tel = request.json['num_tel']
    direccion = request.json['direccion']

    new_pasajero = Pasajero(nombre, apellido, email, num_tel,direccion)
    db.session.add(new_pasajero)
    db.session.commit()
    return jsonify(pasajero_schema.dump(new_pasajero))

@route_pasajeros.route('/updatepasajero', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    email = request.json['email']
    num_tel = request.json['num_tel']
    direccion = request.json['direccion']

    pasajero = Pasajero.query.get(id)
    if pasajero :
        print(pasajero)
        pasajero.nombre = nombre
        pasajero.apellido = apellido
        pasajero.email = email
        pasajero.num_tel = num_tel
        pasajero.direccion = direccion
        db.session.commit()
        return jsonify(pasajero_schema.dump(pasajero))
    else:
        return "Error"

@route_pasajeros.route('/deletepasajero/<id>', methods=['DELETE'])
def delete(id):
    pasajero = Pasajero.query.get(id)
    db.session.delete(pasajero)
    db.session.commit()
    return jsonify(pasajero_schema.dump(pasajero))
