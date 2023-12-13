
from flask import Flask
from flask import flash
from flask import request
from flask import render_template
from flask import redirect

from database import Database
from database import engine
from database import db_session
from flask import url_for

import models

app = Flask(__name__)
    
Database.metadata.create_all(engine)

@app.get('/') 
def home():   
    producto = db_session.query(models.productos).all()
    return render_template("home.html", lista_productos=producto)

@app.get('/inicio') 
def inicio():   
    return render_template("Inicio.html")


@app.get('/subir') 
def subir():   
    return render_template("/plantillas/formulario.html")

@app.get('/presentacion') 
def present():   
    return render_template("presentacion.html")

@app.post('/insertar')
def insertar():
    name = request.form['nombre']
    pre = request.form['precio']
    cant = request.form['cantidad']
    pre_m = request.form['precio_mayoreo']
    status = request.form['estatus']
    
    nuevo_producto = models.productos(
        nombre = name,
        precio = pre,
        cantidad = cant,
        precio_mayoreo = pre_m,
        estatus = status,
    )
    db_session.add(nuevo_producto)
    db_session.commit()
    return redirect("/")

@app.get('/eliminar/<id>')
def eliminar(id):
   producto = db_session.query(models.productos).get(id)
   
   if producto == None:
       flash('ID no encontrado')
       return render_template('home.html')
   
   db_session.delete(producto)
   db_session.commit()
   
   return redirect(url_for('home'))  
   
@app.post('/actualizar/<id>')
def actualizar(id):
    producto = db_session.query(models.productos).get(id)
       
    if producto == None:
        flash('ID no encontrado')
        return redirect (url_for('home'))
       
    nomb = request.form['name']
    pre = request.form['pre_a']
    cant = request.form['cant_a']
    pre_m = request.form['pre_m_a']
    status = request.form['sta_a']
       
    if producto == None:
        flash('No hay nada')
        return redirect (url_for('home'))
       
    producto.nombre = nomb
    producto.precio = pre
    producto.cantidad = cant
    producto.precio_mayoreo=pre_m
    producto.estatus = status
       
    db_session.add(producto)
    db_session.commit()
       
    return redirect(url_for('home'))
   
   
   
if __name__ == '__main__':
    app.run('0.0.0.0', 6565, debug=True)
    

    