# -*- coding: utf-8 -*-
from bottle import route, default_app, template, static_file, get, post, request, run
import funciones

@route('/')
def index():
	return template('index.tpl')

@route('/informacion')
@route('/informacion/')
def informacion():
	return template('informacion.tpl')

@get('/infowiki')
@post('/infowiki')
def infowiki():
	categoria = request.params.get('category')
	busqueda = request.params.get('busqueda')
	imagen = funciones.urlimagen(busqueda)
	titulo = funciones.obtentitulo(busqueda)
	#Para evitar recibir una respuesta en formato Wikitext, he optado por usar markdown para convertir el formato
	funciones.textowiki(busqueda)
	return template("infowiki.tpl", {"imagen":imagen, "titulo":titulo})

@route('/static/<filename>')
def serve_filename(filename):
	return static_file(filename, root=os.environ['OPENSHIFT_REPO_DIR']+"wsgi/static")

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=os.environ['OPENSHIFT_REPO_DIR']+"wsgi/static")

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
