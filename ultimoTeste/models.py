from ultimoTeste import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_e_sobrenome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Cliente('{self.nome_e_sobrenome}', '{self.email}', '{self.celular}', '{self.sexo}')"
