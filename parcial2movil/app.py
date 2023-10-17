from flask import Flask, jsonify, json
from config.db import db, ma, app
from api.ciudad import Ciudad, route_ciudades
from api.conductor import Conductor, route_conductores
from api.pago import Pago, route_pagos
from api.resena import Resena, route_resenas
from api.solicitud import Solicitud, route_solicitud
from api.vehiculo import Vehiculo, route_vehiculos
from api.viaje import Viaje, route_viajes

app.register_blueprint(route_ciudades, url_prefix="/api")

app.register_blueprint(route_conductores, url_prefix="/api")

app.register_blueprint(route_pagos, url_prefix="/api")

app.register_blueprint(route_resenas, url_prefix="/api")

app.register_blueprint(route_solicitud, url_prefix="/api")

app.register_blueprint(route_vehiculos, url_prefix="/api")

app.register_blueprint(route_viajes, url_prefix="/api")


@app.route("/")
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
