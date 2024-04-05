# from app import app , categorias 
# from flask import flash , render_template , request , jsonify
# import pymongo
# from bson.json_util import dumps

# @app.route ("/obtenerCategorias")
# def obtenerCategorias():
#          cat= categorias.find()
#          listaCategorias = list(cat)
#          json_data = dumps(listaCategorias)
#          print(json_data)
#          retorno = {"categorias": json_data}
#          return jsonify(retorno)

# //////////////////////////////////

# from app import app, categoria
# from flask import Flask, render_template, request, jsonify
# import pymongo
# from bson.json_util import dumps

# @app.route ("/obtenerCategorias")
# def obtenerCategorias():
#     cat = categoria.find()
#     listaCategorias = list (cat)
#     json_data = dumps(listaCategorias)
#     print(json_data)
#     retorno = {"categorias":json_data}
#     return jsonify(retorno)