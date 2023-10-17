from config.db import db, ma, app


class Pasajero(db.Model):
    __tablename__ = "pasajeros"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(50))
    num_tel = db.Column(db.Integer())
    direccion = db.Column(db.String(50))

    def __init__(self, nombre, apellido, email, num_tel, direccion):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.num_tel = num_tel
       self.direccion = direccion

with app.app_context():
    db.create_all()

class PasajeroSchema(ma.Schema):
    class Meta:
        fields = ("id","nombre","apellido","email","num_tel","direccion")

