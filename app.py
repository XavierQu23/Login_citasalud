from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Utils.db import db 
from Models.usuario import Usuario

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:123456@localhost/CitaSalud"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.post('/new')
def home():
    name= request.form['nombre']
    apellido= request.form['apellido']
    email= request.form['email']
    clave= request.form['clave']
    new_usuario= Usuario(name,apellido,email,clave)
    db.session.add(new_usuario)
    db.session.commit()
    return ' new hello world'



@app.route('/login',methods=['POST','GET'])
def index():
    usuarios = Usuario.query.all()
    if request.method== "POST":
        email= request.form['email']
        clave= request.form['clave']
        for usuario in usuarios:
            if usuario.email== email and usuario.clave==clave:
                return render_template("index.html")  
            else:
                return render_template("login.html")
    return render_template("login.html")

@app.route('/registro')
def formulario():
    return render_template('registro.html')

@app.route('/login')
def list():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug = True, port = 5001)