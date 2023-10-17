from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.solicitud import Solicitud, SolicitudSchema

route_solicitud = Blueprint("route_solicitudes", __name__)

solicitud_schema = SolicitudSchema()
Solicitudes_schema = SolicitudSchema(many=True)


@route_solicitud.route("/solicitudes", methods=["GET"])
def solicitud():
    resultall = Solicitud.query.all()  
    resultado_solicitud = solicitud_schema.dump(resultall)
    return jsonify(resultado_solicitud)


@route_solicitud.route("/savesolicitud", methods=["POST"])
def save():
    pasajero_id = request.json["pasajero_id"]
    asignado = request.json["asignado"]

    new_solicitud = Solicitud(pasajero_id, asignado)
    db.session.add(new_solicitud)
    db.session.commit()
    return jsonify(solicitud_schema.dump(new_solicitud))

@route_solicitud.route("/updatesolicitud", methods=["PUT"])
def update():
    id = request.json["id"]
    pasajero_id = request.json["pasajero_id"]
    asignado = request.json["asignado"]
    solicitud = Solicitud.query.get(id)
    if solicitud:
        print(solicitud)
        solicitud.pasajero_id = pasajero_id
        solicitud.asignado = asignado
        db.session.commit()
        return jsonify(solicitud_schema.dump(solicitud))
    else: 
        return "Error"
    
@route_solicitud.route("/deletesolicitud/<id>", methods=["DELETE"])
def delete(id):
    solicitud = Solicitud.query.get(id)
    db.session.delete(solicitud)
    db.session.commit()
    return jsonify(solicitud_schema.dump(solicitud))

