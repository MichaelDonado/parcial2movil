from config.db import db, ma, app


class Viaje(db.Model):
    __tablename__ = "viajes"

    id = db.Column(db.Integer, primary_key=True)
    vehiculo = db.Column(db.Integer, db.ForeignKey('vehiculos.id'))
    inicio = db.Column(db.DateTime, nullable=False)
    fin = db.Column(db.DateTime, nullable=False)
    ruta = db.Column(db.String(255), nullable=False)
    solicitud_id = db.Column(db.Integer, db.ForeignKey('solicitudes.id'), nullable=False)

    def __init__ (self, vehiculo, inicio, fin, ruta, solicitud_id):
        self.vehiculo = vehiculo
        self.inicio = inicio
        self.fin = fin
        self.ruta = ruta
        self.solicitud_id = solicitud_id
    

with app.app_context():
    db.create_all()


class ViajeSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "vehiculo",
            "inicio",
            "fin",
            "ruta",
            "solicitud_id", 
        )
