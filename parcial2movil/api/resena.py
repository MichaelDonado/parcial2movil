from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.resena import Resena, ResenaSchema

route_resenas = Blueprint("route_resenas", __name__)

resena_schema = ResenaSchema()
resenas_schema = ResenaSchema(many=True)

@route_resenas.route('/resenas', methods=['GET'])
def resena():
    resultall = Resena.query.all()
    result_resena = resenas_schema.dump(resultall)
    return jsonify(result_resena)

@route_resenas.route('/saveresena', methods=['POST'])
def save():
    puntuacion = request.json['puntuacion']
    comentario = request.json['comentario']
    viaje_id = request.json['viaje_id']
    

    new_resena = Resena(puntuacion, comentario, viaje_id)
    db.session.add(new_resena)
    db.session.commit()
    return jsonify(resena_schema.dump(new_resena))

@route_resenas.route('/updateresena', methods=['PUT'])
def Update():
    id = request.json['id']
    puntuacion = request.json['puntuacion']
    comentario = request.json['comentario']
    viaje_id = request.json['viaje_id']
    resena = Resena.query.get(id)
    if resena :
        print(resena)
        resena.puntuacion = puntuacion
        resena.comentario = comentario
        resena.viaje_id = viaje_id
        db.session.commit()
        return jsonify(resena_schema.dump(resena))
    else:
        return "Error"

@route_resenas.route('/deleteresena/<id>', methods=['DELETE'])
def delete(id):
    resena = Resena.query.get(id)
    db.session.delete(resena)
    db.session.commit()
    return jsonify(resena_schema.dump(resena))
