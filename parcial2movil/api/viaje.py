from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.viaje import Viaje, ViajeSchema

route_viajes = Blueprint("route_viajes", __name__)

viaje_schema = ViajeSchema()
viajes_schema = ViajeSchema(many=True)

@route_viajes.route('/viajes', methods=['GET'])
def viaje():
    result_all = Viaje.query.all()
    result_viajes = viajes_schema.dump(result_all)
    return jsonify(result_viajes)

@route_viajes.route('/saveviaje', methods=['POST'])
def save():
    vehiculo = request.json['vehiculo']
    inicio = request.json['inicio']
    fin = request.json['fin']
    ruta = request.json['ruta']
    solicitud_id = request.json['solicitud_id']

    new_viaje = Viaje(vehiculo, inicio, fin, solicitud_id, ruta)
    db.session.add(new_viaje)
    db.session.commit()
    return jsonify(viaje_schema.dump(new_viaje))

@route_viajes.route('/updateviaje', methods=['PUT'])
def update():
    id = request.json['id']
    vehiculo = request.json['vehiculo']
    inicio = request.json['inicio']
    fin = request.json['fin']
    ruta = request.json['ruta']
    solicitud_id = request.json['solicitud_id']
    viaje = Viaje.query.get(id)
    if viaje:
        viaje.vehiculo = vehiculo
        viaje.inicio = inicio
        viaje.fin = fin
        viaje.ruta = ruta
        viaje.solicitud_id = solicitud_id
        db.session.commit()
        return jsonify(viaje_schema.dump(viaje))
    else:
        return "Error"

@route_viajes.route('/deleteviaje/<id>', methods=['DELETE'])
def delete(id):
    viaje = Viaje.query.get(id)
    db.session.delete(viaje)
    db.session.commit()
    return jsonify(viaje_schema.dump(viaje))
