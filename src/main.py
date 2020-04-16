from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
PORT = 5000
DEBUG = False
CORS(app)


try:
    conn = psycopg2.connect(dbname="d7cp5alf3f29d6", user="rplunjajsfzxwx",
                            password="7eec3bdb7f6079b1dc3776c7d0396bb54d042b9753189ae92cb33ff724fce4db", host="ec2-3-223-21-106.compute-1.amazonaws.com", port="5432")
except Exception as e:
    print(e)


@app.errorhandler(404)
def notFound():
    return "Not Found"


@app.route("/", methods=["GET"])
def index():
    with conn.cursor() as cursor:
        query = '''SELECT * FROM Usuarios'''
        cursor.execute(query)
        row = cursor.fetchall()
        payload = []
        content = {}
        for element in row:
            content = {
                'Id': element[0],
                'nombre': element[1],
                'apellido_paterno': element[2],
                'apellido_materno': element[3],
                'telefono': element[4],
                'direccion': element[5],
                'delegacion': element[6],
                'municipio': element[7],
                'estado': element[8],
                'email': element[9],
                'pwd': element[10],
                'rol': element[11]
            }
            payload.append(content)
            content = {}
        return jsonify(payload)
        conn.commit()
        conn.close()
# ----------------------------------------Usuarios
@app.route("/api/Login", methods=["POST"])
def postLogin():
    if request.method == 'POST':
        email = request.json['email']
        pwd = request.json['pwd']
        try:
            with conn.cursor() as cursor:
                query = '''SELECT Id,nombre,delegacion,municipio,estado,rol FROM Usuarios WHERE email=%s AND pwd =%s'''
                cursor.execute(query, (email, pwd))
                row = cursor.fetchone()
                payload = []
                content = {
                    'Id': row[0],
                    'Nombre': row[1],
                    'Delegacion': row[2],
                    'Municipio': row[3],
                    'Estado': row[4],
                    'Rol': row[5]
                }
                payload.append(content)
            return jsonify(payload)
        except Exception as e:
            return jsonify(e)
        finally:
            conn.commit()
            conn.close()


@app.route("/api/Registro/Usuario", methods=["POST"])
def postRegistro():
    if request.method == 'POST':
        nombre = request.json['nombre']
        apellido_paterno = request.json['apellido_paterno']
        apellido_materno = request.json['apellido_materno']
        telefono = request.json['telefono']
        direccion = request.json['direccion']
        delegacion = request.json['delegacion']
        municipio = request.json['municipio']
        estado = request.json['estado']
        email = request.json['email']
        pwd = request.json['pwd']
        rol = request.json['rol']
        try:
            with conn.cursor() as cursor:
                query = '''INSERT INTO Usuarios (nombre, apellido_paterno, apellido_materno, telefono, direccion, delegacion, municipio, estado, email, pwd, rol) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                cursor.execute(query, (nombre, apellido_paterno,
                                       apellido_materno, telefono, direccion, delegacion, municipio, estado, email, pwd, rol))
            return jsonify({"message": "datos guardados"})
        except Exception as e:
            return jsonify(e)
        finally:
            conn.commit()
            conn.close()


@app.route("/api/Usuario/", methods=["PUT"])
def putActualizar():
    if request.method == 'PUT':
        Id = request.json['Id']
        nombre = request.json['nombre']
        apellido_paterno = request.json['apellido_paterno']
        apellido_materno = request.json['apellido_materno']
        telefono = request.json['telefono']
        direccion = request.json['direccion']
        delegacion = request.json['delegacion']
        municipio = request.json['municipio']
        estado = request.json['estado']
        try:
            with conn.cursor() as cursor:
                query = '''UPDATE Usuarios SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, telefono=%s, direccion=%s, delegacion=%s, municipio=%s, estado=%s WHERE Id=%s'''
                cursor.execute(query, (nombre, apellido_paterno,
                                       apellido_materno, telefono, direccion, delegacion, municipio, estado, Id))
            return jsonify({"message": "datos guardados"})
        except Exception as e:
            return jsonify(e)
        finally:
            conn.commit()
            conn.close()
        return jsonify({"message": "respuesta"})


@app.route("/api/Usuario", methods=["DELETE"])
def deleteUsuario():
    if request.method == 'DELETE':
        Id = request.json['Id']
        try:
            with conn.cursor() as cursor:
                query = '''DELETE FROM Usuarios WHERE Id=%s'''
                cursor.execute(query, (Id))
            return jsonify({"message": "datos eliminados"})
        except Exception as e:
            return jsonify(e)
        finally:
            conn.commit()
            conn.close()
        return jsonify({"message": "respuesta"})


# ----------------------------------------Publicaciones
@app.route("/api/Registro/Publicacion/<string:Id>", methods=["POST"])
def postPub(Id):
    if request.method == 'POST':
        nombre = request.json['nombre']
        tipo = request.json['tipo']
        costo = request.json['costo']
        comentarios = request.json['comentarios']
        horario = request.json['horario']
        telefono = request.json['telefono']
        direccion = request.json['direccion']
        delegacion = request.json['delegacion']
        municipio = request.json['municipio']
        estado = request.json['estado']
        email = request.json['email']

        try:
            with conn.cursor() as cursor:
                query = '''INSERT INTO Servicios (nombre,tipo,costo,comentarios,horario,telefono,direccion,delegacion,municipio,estado,email,Usuario) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                cursor.execute(query, (nombre, tipo, costo, comentarios, horario,
                                       telefono, direccion, delegacion, municipio, estado, email, Id))
            return jsonify({"message": "datos guardados"})
        except Exception as e:
            return jsonify(e)
        finally:
            conn.commit()
            conn.close()


@app.route("/api/Publicacion", methods=["PUT"])
def putPub():
    if request.method == 'PUT':

        return jsonify({"message": "respuesta"})


@app.route("/api/Publicacion", methods=["DELETE"])
def deletePub():
    if request.method == 'DELETE':

        return jsonify({"message": "respuesta"})


@app.route("/api/Publicacion/Buscar", methods=["POST"])
def postBuscar():
    if request.method == 'POST':

        return jsonify({"message": "respuesta"})


@app.route("/api/Publicacion/Calificar", methods=["POST"])
def postCalificar():
    if request.method == 'POST':

        return jsonify({"message": "respuesta"})


@app.route("/api/Publicacion/Comentar", methods=["POST"])
def postComentar():
    if request.method == 'POST':

        return jsonify({"message": "respuesta"})

# ----------------------------------------Servicios
@app.route("/api/Servicios", methods=["GET"])
def getServicios():
    if request.method == 'GET':

        return jsonify({"message": "respuesta"})


@app.route("/api/Servicios/<string:tipo>", methods=["GET"])
def getServiciosTipo(tipo):
    if request.method == 'POST':

        return jsonify({"message": "respuesta"})


@app.route("/api/Servicios/Ubicación", methods=["GET"])
def getServiciosUbicacion():
    if request.method == 'GET':

        return jsonify({"message": "respuesta"})


# starting the app
if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
