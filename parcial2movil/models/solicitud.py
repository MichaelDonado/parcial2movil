from config.db import db, ma, app


class Solicitud(db.Model):
    __tablename__ = "solicitudes"

    id = db.Column(db.Integer, primary_key=True)
    pasajero_id = db.Column(db.Integer, db.ForeignKey('pasajeros.id'), nullable=False)
    asignado = db.Column(db.Boolean, default=False)

    def __init__(self, pasajero_id, asignado):
        self.pasajero_id = pasajero_id
        self.asignado = asignado

with app.app_context():
    db.create_all()


class SolicitudSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "pasajero_id",
            "asignado",
        )
