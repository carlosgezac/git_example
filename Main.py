from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host = 'bvvmj4zd488jdbbc8toa-mysql.services.clever-cloud.com',
    port = 3306,
    user = 'ue3bsszlvebklwhn',
    password = 'obKo2LGCRIKLfpQHOc0S',
    db = 'bvvmj4zd488jdbbc8toa'
)

#variable de sesion
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    connection.ping()  # reconnecting mysql
    cursor = connection.cursor()
    sql = "SELECT * FROM contacts"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', contacts = data) #Esta pasando los datos en 'contacts' para ser mostrados en index.html

@app.route('/add-contact', methods=['POST'])
def addContact():
    if request.method == 'POST':
        #PARAMETROS peticion HTTP
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        #Abrir cursor mysql, ejecutar query y cerrar conexion
        connection.ping()  # reconnecting mysql
        cursor = connection.cursor()
        sql = "INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (fullname, phone, email))
        connection.commit() #persistir
        cursor.close() #cerrar conexion
        flash('Contact added successfully.') #flash utilizado para emnsajes entre vistas
        return redirect(url_for('index')) #index, es el nombre la funcion

@app.route('/edit-contact/<string:id>', methods=['GET'])
def editContact(id):
    if request.method == 'GET':
        connection.ping()  # reconnecting mysql
        cursor = connection.cursor()
        sql = "SELECT * FROM contacts WHERE id = {}".format(id)
        cursor.execute(sql)
        contact = cursor.fetchone()
        cursor.close()
        return render_template('edit-contact.html', contact = contact)
    

@app.route('/update-contact/<id>', methods=['POST'])
def updateContact(id):
     if request.method == 'POST':
        #PARAMETROS peticion HTTP
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        #Abrir cursor mysql, ejecutar query y cerrar conexion
        connection.ping()  # reconnecting mysql
        cursor = connection.cursor()
        sql = "UPDATE contacts SET fullname = '{}', phone = '{}', email = '{}' WHERE id = {}" .format(fullname, phone, email, id)
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        flash('Contact modified successfully.') #flash utilizado para emnsajes entre vistas
        return redirect(url_for('index')) #index, es el nombre la funcion

@app.route('/delete-contact/<string:id>')
def deleteContact(id):
    print(id)
    connection.ping()  # reconnecting mysql
    cursor = connection.cursor()
    sql = "DELETE FROM contacts WHERE id ={}".format(id)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    flash('Contact removed successfully')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html') #Esta pasando los datos en 'contacts' para ser mostrados en index.html

if __name__ == '__main__':
    app.run(port = 5000, debug = True)