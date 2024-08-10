from db import db


class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(25), nullable=False)
    
    
    def __repr__(self):
        return f"{self.nome}"