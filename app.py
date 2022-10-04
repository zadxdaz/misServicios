from flask import Flask
from flask_restful import Api, Resource
from database import User,Servicios
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def nuevoUsuario():
    return "<p>Nuevo Usuario</p>"

def nuevoServicio():
    return "<p>Nuevo Servicio</p>"

def listaServicios():
    return "<p>Los servicios</p>"
