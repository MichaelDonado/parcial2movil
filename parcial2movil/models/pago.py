from config.db import db, ma, app


class Pago(db.Model):
    __tablename__ = "pagos"

    id = db.Column(db.Integer, primary_key=True)
    pasajeros_id = db.Column(db.Integer, db.ForeignKey("pasajeros.id"))
    metodo_pago = db.Column(db.String(200))
    pago_total = db.Column(db.Double)

    def __init__(self, pasajeros_id, metodo_pago, pago_total): 
        self.pasajeros_id = pasajeros_id
        self.metodo_pago = metodo_pago
        self.pago_total = pago_total

with app.app_context():
    db.create_all()


class PagoSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "pasajeros_id",
            "metodo_pago",
            "pago_total",
        )
