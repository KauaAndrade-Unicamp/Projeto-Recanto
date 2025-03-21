from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_migrate import Migrate 

load_dotenv()

app = Flask(__name__)

database_url = os.getenv('DATABASE_URL')

if not database_url:
    raise ValueError("A variável de ambiente DATABASE_URL não está definida.")

if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
    
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # ✅ Agora está correto

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    nome = db.Column(db.String(120))

@app.route('/')
def getpalavra():
    return "Sabrina Meu Amor"

if __name__ == '__main__':
    app.run(port=3000, debug=True)
