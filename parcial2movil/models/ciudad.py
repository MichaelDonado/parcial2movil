from config.db import  db, ma, app

class Ciudad(db.Model):
    __tablename__ = "ciudades"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    departamento = db.Column(db.String(50))
    origen = db.Column(db.String(50))
    destino = db.Column(db.String(50))

    def __init__(self, nombre, departamento, origen, destino):
        self.nombre = nombre
        self.departamento = departamento
        self.origen = origen
        self.destino = destino

with app.app_context():
    db.create_all()

class CiudadSchema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "departamento", "origen", "destino")