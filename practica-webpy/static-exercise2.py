# -*- encoding: utf-8 -*-
import web
        
# Asocia cualquier ruta url con la clase 'hola'
urls = (
	'/(.*)', 'hola'  # Expresión regular, clase asociada
)
app = web.application(urls, globals())

class hola:        
	# name es el contenido del primer paréntesis    
	def GET(self, name):    # petición GET
		if not name:  name = 'mundo'
		return "<html> <head></head><body><h1>Hola!</h1></body>"

# Para que se ejecute como aplicación independiente 
# con el servidor de web propio
if __name__ == "__main__":
	app.run()