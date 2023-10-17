from config.db import db, ma, app


class Conductor(db.Model):
    __tablename__ = "conductores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    telefono = db.Column(db.String(10))
    licencia  = db.Column(db.Boolean, default=True)

    def __init__(self, nombre, apellido, telefono, licencia):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.licencia = licencia


with app.app_context():
    db.create_all()


class ConductorSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre",
            "apellido",
            "telefono",
            "licencia"
        )
