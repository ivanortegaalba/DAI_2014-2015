#encoding:utf-8
'''
Created on 26/1/2015

@author: ivanortegaalba
'''

# -*- encoding: utf-8 -*-
import web
from web import form
        
# Asocia cualquier ruta url con la clase 'hola'
urls = (
    '/(.*)', 'hola'  # Expresión regular, clase asociada
)
form.Form(form.Textbox('usuario'),
		form.Button('enviar')
		)

app = web.application(urls, globals())



class hola:        
	
	
    # name es el contenido del primer paréntesis    
    def GET(self):    # petición GET
        

# Para que se ejecute como aplicación independiente 
# con el servidor de web propio
if __name__ == "__main__":
    app.run()