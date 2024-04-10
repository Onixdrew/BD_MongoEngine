from mongoengine import Document, ReferenceField, StringField,BinaryField, IntField,EmailField

class usuarios(Document):
    nombre=StringField(max_length=50)
    correo=EmailField(required=True, unique=True)
    contraseña=StringField(max_length=50)

class categorias(Document):
    nombre=StringField(max_length=50, unique=True)

class productos(Document):
    codigo=IntField(unique=True)
    nombre=StringField(max_length=50)
    precio=IntField()
    categoria=ReferenceField(categorias)
    # convierte la imagen a binario
    foto = BinaryField()
    
