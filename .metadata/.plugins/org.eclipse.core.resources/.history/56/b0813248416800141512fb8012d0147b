# -*- encoding: utf-8 -*-
import web

# Asocia cualquier ruta url con la clase 'css'
urls = (
	'/(.*)', 'css'  # Expresión regular, clase asociada
)
app = web.application(urls, globals())

class css:
	# name es el contenido del primer paréntesis
	def GET(self, name):    # petición GET
		if not name:  name = 'mundo'
		return '<html> \
		<head>\
		<link rel="stylesheet" type="text/css" href="./hoja-exercise3.css" media="screen"/>\
		</head>\
		<body>\
		<h1>Mostrando imagenes estáticas con hojas de estilo</h1>\
		<img href="./static/images/estatica1f.png">\
		</body>'


# Para que se ejecute como aplicación independiente
# con el servidor de web propio
if __name__ == "__main__":
	app.run()
