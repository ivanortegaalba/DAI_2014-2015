# -*- encoding: utf-8 -*-
import web
from web import form
from web.contrib.template import render_mako

web.config.debug = False

render = web.template.render('templates/')

urls = ('/', 'index',
		'/pagina1', 'pagina1',
		'/pagina2', 'pagina2',
		'/pagina3', 'pagina3',
		'/pagina4', 'pagina4',
		'/salir','cerrarSesion')

app = web.application(urls, locals(),autoreload=False)

makos = render_mako(
		directories=['templates'],
		input_encoding='utf-8',
		output_encoding='utf-8')

session = web.session.Session(app, 
	  web.session.DiskStore('sessiones'))

login = form.Form(
	form.Textbox('Usuario', class_="form-control"),
	form.Password('Contrasena', class_="form-control"),
	form.Checkbox('Recuerdame', 
				  value='true'),
	form.Button('Entrar', _class="button btn-default"))

mensaje = ",  Bienvenido.  <a href='/salir'>Salir</a>" 

def insertarUltimaPagina(ultima):
	session.pag3 = session.pag2
	session.pag2 = session.pag1
	session.pag1 = str(ultima)
	
contentbody= "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero, adarga antigua, rocin flaco y galgo corredor."

def mostrarUltimas():
	return"\
			<li>" + str(session.pag1) + "</li> \
			<li>" + str(session.pag2) + "</li> \
			<li>" + str(session.pag3) +"</li>"
 
class index:
	paginaActual = "Inicio"
	def GET(self):
		if 'user' not in session:
			loginForm = login();
			return makos.mako_template(varDep = "",titulo = self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		if not loginForm.validates():
			return makos.mako_template(varDep = "",titulo = self.paginaActual, form = loginForm)		
		else:
			input_t = web.input()
			user = input_t.Usuario
			session.user = user
			session.pag1 = "null"
			session.pag2 = "null"
			session.pag3 = "null"
			return makos.mako_template(varDep = "",titulo = self.paginaActual, mensaje = (session.user) + mensaje)

class pagina1:
	paginaActual = "Pagina 1"
	def GET(self):
		if 'user' not in session:
			loginForm=login();
			return makos.mako_template(varDep = "",titulo =self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		if not loginForm.validates():
			return makos.mako_template(varDep = "",form = loginForm)		
		else:
			input_t = web.input()
			user = input_t.Usuario
			session.user = user
			session.pag1 = "null"
			session.pag2 = "null"
			session.pag3 = "null"
			return makos.mako_template(varDep = "",titulo = self.paginaActual, mensaje = (session.user) + mensaje)

class pagina2:
	paginaActual = "Pagina 2"
	
	def GET(self):
		if 'user' not in session:
			loginForm =login();
			return makos.mako_template(varDep = "",titulo =self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		if not loginForm.validates():
			return makos.mako_template(varDep = "",form = loginForm)		
		else:
			input_t = web.input()
			user = input_t.Usuario
			session.user = user
			session.pag1 = "null"
			session.pag2 = "null"
			session.pag3 = "null"
			return makos.mako_template(varDep = "",titulo =self.paginaActual, mensaje = (session.user) + mensaje)

class pagina3:
	paginaActual = "Pagina 3"
	def GET(self):
		if 'user' not in session:
			loginForm = login();
			return makos.mako_template(varDep = "",titulo =self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		if not loginForm.validates():
			return makos.mako_template(varDep = "",form = loginForm)		
		else:
			input_t = web.input()
			user = input_t.Usuario
			session.user = user
			session.pag1 = "null"
			session.pag2 = "null"
			session.pag3 = "null"
			return makos.mako_template(varDep = "",titulo =self.paginaActual, mensaje = (session.user) + mensaje)

class pagina4:
	paginaActual = "Pagina 4"
	def GET(self):
		if 'user' not in session:
			loginForm = login();
			return makos.mako_template(varDep = "",titulo =self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		if not loginForm.validates():
			return makos.mako_template(varDep = "",form = loginForm)		
		else:
			input_t = web.input()
			user = input_t.Usuario
			session.user = user
			session.pag1 = "null"
			session.pag2 = "null"
			session.pag3 = "null"
			return makos.mako_template(varDep = "",titulo =self.paginaActual, mensaje = (session.user) + mensaje)

class cerrarSesion:
	def GET(self):
		session.kill()
		raise web.seeother('/')

if __name__=="__main__":
	web.internalerror = web.debugerror
	app.run()
