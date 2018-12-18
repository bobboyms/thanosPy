from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456789@localhost/teste"
db = SQLAlchemy(app)

app.debug = True

# class Cliente(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome = db.Column(db.String(80), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.nome

# cliente = Cliente()
# cliente.nome = "pedro jose"

# db.session.add(cliente)
# db.session.commit()
