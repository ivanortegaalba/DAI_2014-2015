# -*- encoding: utf-8 -*-

import web

urls = (
	'/hola(.*)', 'hola',
	'/.*', 'nofound'
)

app =  web.application(urls, globals())

class hola:
	# name es el contenido del primer paréntesis
	def GET(self, name):    # petición GET
		if not name:  name = 'mundo'
		return "<html> <head></head><body><h1>Hola" + name + "!</h1></body>"

def notfound():
    return web.notfound("Sorry, the page you were looking for was not found.")

    # You can use template result like below, either is ok:
    #return web.notfound(render.notfound())
    #return web.notfound(str(render.notfound()))

app.notfound = notfound

class nofound:
    def GET(self):
        raise web.notfound()

# Para que se ejecute como aplicación independiente
# con el servidor de web propio
if __name__ == "__main__":
	app.run()
