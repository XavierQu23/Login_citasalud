from Utils.db import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(100))
    clave = db.Column(db.String(100))
                                                         
    def __init__(self, nombre, apellido, email, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.clave = clave
        
         
         
         
         