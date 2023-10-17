from config.db import db, ma, app


class Resena(db.Model):
    __tablename__ = "resenas"

    id = db.Column(db.Integer, primary_key=True)
    puntuacion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(255))
    viaje_id = db.Column(db.Integer, db.ForeignKey('viajes.id'), nullable=False)

    def __init__(self, puntuacion, comentario, viaje_id): 
        self.puntuacion = puntuacion
        self.comentario = comentario
        self.viaje_id = viaje_id

with app.app_context():
    db.create_all()


class ResenaSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "puntuacion",
            "comentario",
            "viaje_id",
        )
