from flask import Flask
import mongoengine

# crear aplicación
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'GestionProductos',
}

app.config["UPLOAD_FOLDER"] = "./static/imagenes"


miConexion=mongoengine.connect(host='mongodb+srv://Andrew:6yRZzkGdCsFPGPs0@cluster0.qj0gkdd.mongodb.net/GestionProductos')
usuarios = miConexion['usuarios']
productos = miConexion['productos']
categorias = miConexion['categorias']



# Creo clave para manejar la sesión
app.secret_key = "codeUltronixSecure"

# Crear conexión con MongoDB
# miConexion = pymongo.MongoClient('mongodb+srv://Andrew:6yRZzkGdCsFPGPs0@cluster0.qj0gkdd.mongodb.net/')
# baseDatos = miConexion['GestionProductos']

# Importar modelos(clases) definidos con mongoengine
from models.model import *

# importo la carpeta llamada controlador y al archivo que contiene
from controlador.productocontroller import *

# arranco la aplicacion
if __name__=='__main__':
    app.run(port=3000, debug=True)