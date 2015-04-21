from bottle import route, default_app, template, static_file, get, post, request

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
	categoria = bottle.request.params.get('category')
	busqueda = bottle.request.params.get('busqueda')
	urlapi = "http://es.wikipedia.org/w/api.php?"
	if categoria == 1:
		jsonfile = requests.get(apiurl + "action=query&prop=pageimages&format=json&piprop=original&titles=" + busqueda)
		archivo = json.load(jsonfile)
		for campos in archivo["query"]["pages"]:
			urlimagen = str(campos["title"]["original"])
	return urlimagen



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
