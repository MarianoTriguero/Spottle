from bottle import route, default_app, template, static_file

@route('/')
def index():
	return template('header.tpl')
	return template('index.tpl')
	return template('footer.tpl')

@route('/informacion/')
def informacion():
	return template('informacion.tpl')

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
