from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask('Murder')
app.config['SQLALCHEMY_DATABASE_URI'] =  'postgresql://postgres:password@localhost:5432/murder'

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

class role(db.Model):
    __tablname__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    biography: Mapped[str] = mapped_column(db.String, unique=False, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/elements.html')
def elements():
    return render_template('elements.html')
@app.route('/generic.html')
def generic():
    return render_template('generic.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(host="192.168.0.10", port=8000)

