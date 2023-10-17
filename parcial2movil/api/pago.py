from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.pago import Pago, PagoSchema

route_pagos = Blueprint("route_pagos", __name__)

pago_schema = PagoSchema()
pagos_schema = PagoSchema(many=True)

@route_pagos.route('/pagos', methods=['GET'])
def pago():
    result_all = Pago.query.all()
    result_pagos = pagos_schema.dump(result_all)
    return jsonify(result_pagos)

@route_pagos.route('/savepago', methods=['POST'])
def save():
    pasajero_id = request.json['pasajero_id']
    metodo_pago = request.json['metodo_pago']
    pago_total = request.json['pago_total']
    

    new_pago = Pago(pasajero_id, metodo_pago, pago_total)
    db.session.add(new_pago)
    db.session.commit()
    return jsonify(pago_schema.dump(new_pago))

@route_pagos.route('/updatepago', methods=['PUT'])
def update():
    id = request.json['id']
    pasajero_id = request.json['pasajero_id']
    metodo_pago = request.json['metodo_pago']
    pago_total = request.json['pago_total']
    pago = Pago.query.get(id)
    if pago:
        pago.pasajero_id = pasajero_id
        pago.metodo_pago = metodo_pago
        pago.pago_total = pago_total
        db.session.commit()
        return jsonify(pago_schema.dump(pago))
    else:
        return "Error"

@route_pagos.route('/deletepago/<id>', methods=['DELETE'])
def delete(id):
    pago = Pago.query.get(id)
    db.session.delete(pago)
    db.session.commit()
    return jsonify(pago_schema.dump(pago))


