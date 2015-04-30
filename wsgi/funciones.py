# -*- coding: utf-8 -*-
import json
import urllib
import re
from bs4 import BeautifulSoup
import markdown

def transformaesp(cadena):
	cadena = cadena.replace(" ", "%20")
	return cadena

def urlimagen(cadena):
	cadena = transformaesp(cadena)
	entradajson = urllib.urlopen("http://es.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles=" + str(cadena))
	archivojson = json.load(entradajson)
	for campos in archivojson["query"]["pages"]:
		imagen = archivojson["query"]["pages"][str(campos)]["thumbnail"]["original"]
	return imagen

def obtentitulo(cadena):
	cadena = transformaesp(cadena)
	entradajson = urllib.urlopen("http://es.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles=" + str(cadena))
	archivojson = json.load(entradajson)
	for campos in archivojson["query"]["pages"]:
		titulo = archivojson["query"]["pages"][str(campos)]["title"]
	return titulo

def textowiki(cadena):
	cadena = transformaesp(cadena)
	# Obtenemos la página en formato imprimible para que sea más fácil su manejo
	textowiki = urllib.urlopen("http://es.wikipedia.org/w/index.php?title=" + str(cadena) + "&printable=yes").read()
	html = markdown.markdown(unicode(textowiki, 'utf-8'))
	html = html.encode('utf-8').strip()
	# Quitamos esta parte para evitar problemas
	html = html.replace("""<td class="ambox-text">Este artículo o sección necesita <b><a href="/wiki/Ayuda:C%C3%B3mo_referenciar" title="Ayuda:Cómo referenciar">referencias</a></b> que aparezcan en una <b><a href="/wiki/Wikipedia:Verificabilidad" title="Wikipedia:Verificabilidad">publicación acreditada</a></b>, como revistas especializadas, monografías, prensa diaria o páginas de Internet <a href="/wiki/Wikipedia:Fuentes_fiables" title="Wikipedia:Fuentes fiables">fidedignas</a>.  Este aviso fue puesto el 4 de agosto de 2011.<br />
<span style="font-size:88%">Puedes <b><a href="/wiki/Ayuda:C%C3%B3mo_referenciar" title="Ayuda:Cómo referenciar">añadirlas</a></b> o avisar <a class="external text" href="//es.wikipedia.org/w/index.php?title=""" + cadena + """&amp;action=history">al autor principal del artículo</a> en su página de discusión pegando: <code>{{subst:Aviso referencias|""" + cadena + """}} ~~~~</code></span></td>""", " ")
	#Obtenemos el texto plano de la página
	soup = BeautifulSoup(html)
	texto = soup.get_text()
	texto = texto.encode('utf-8').strip()
	#Obtenemos la posicion final e inicial de la parte que queremos para formar el documento definitivo
	textoporlineas = texto.splitlines()
	for linea in textoporlineas:
		if str(linea).startswith("[editar datos en Wikidata]"):
			posicioninicio = textoporlineas.index(linea) + 1
		elif "Componentes" == str(linea):
			posicionfinal = textoporlineas.index(linea) - 1
	#Formamos el nuevo documento
	textoelegido = textoporlineas[posicioninicio:posicionfinal]
	texto = ""
	#Ahora recomponemos el texto con las líneas que nos interesan e introducimos el salto de linea para que no se construya como un solo párrafo
	for linea in textoelegido:
	#Descartamos las líneas en blanco
		if str(linea) != "":
			texto = texto + str(linea) + "<br>"
	#Eliminamos los corchetes
	texto = re.sub('\[[0-9][0-9][0-9]\]', ' ', texto)
	texto = re.sub('\[[0-9][0-9]\]', ' ', texto)
	texto = re.sub('\[[0-9]\]', ' ', texto)
	#Escribimos en el archivo
	templ = open("views/wikitext.tpl","w")
	templ.write(texto)
	templ.close()

