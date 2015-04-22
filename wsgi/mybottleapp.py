from bottle import route, default_app, template, static_file, get, post, request

import json
import urllib

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
	busqueda = busqueda.replace(" ", "%20")
	urlapi = "http://es.wikipedia.org/w/api.php?"
	jsontext = urllib.urlopen(str(urlapi) + "action=query&prop=revisions&rvprop=content&format=json&titles=" + str(busqueda))
	jsonimage = urllib.urlopen(str(urlapi) + "action=query&prop=pageimages&format=json&piprop=original&titles=" + str(busqueda))
	archivotext = json.load(jsontext)
	archivoimage = json.load(jsonimage)

	for campos in archivotext["query"]["pages"]:
		texto = archivotext["query"]["pages"][str(campos)]["revisions"][0]["*"]

	for campos in archivoimage["query"]["pages"]:
		imagen = archivoimage["query"]["pages"][str(campos)]["thumbnail"]["original"]
		titulo = archivoimage["query"]["pages"][str(campos)]["title"]
	return template('infowiki.tpl', {"imagen":imagen, "titulo":titulo, "texto":texto})

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
