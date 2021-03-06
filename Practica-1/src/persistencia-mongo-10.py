# -*- encoding: utf-8 -*-
import web
from web import form
from web.contrib.template import render_mako
import anydbm
from pymongo import MongoClient

web.config.debug = True

render = web.template.render('templates/')

urls = ('/', 'index',
		'/pagina1', 'pagina1',
		'/pagina2', 'pagina2',
		'/pagina3', 'pagina3',
		'/pagina4', 'pagina4',
		'/registro', 'Registro',
		'/modificar', 'Modificar'
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

def insertarUltimaPagina(ultima):
	session.pag3 = session.pag2 
	session.pag2 = session.pag1
	session.pag1 = str(ultima)
	
def mostrarUltimas():
	return"\
			<li>" + str(session.pag1) + "</li> \
			<li>" + str(session.pag2) + "</li> \
			<li>" + str(session.pag3) +"</li>"
 
FormularioRegistro = form.Form(
	form.Textbox('Nombre', 
				 form.notnull,
				 class_='form-control'),
	form.Textbox('Apellidos',
				 form.notnull,
				 class_='form-control'),
	form.Textbox('Email',
				 form.notnull,
				 form.regexp('[^@]+@[^@]+\.[^@]+', 'Debe se ser un email'),
				 class_='form-control'),
	form.Dropdown('Dia', 
				  range(1, 31),
				  class_='form-control'),
	form.Dropdown('Mes', 
				  range(1, 12),
				  class_='form-control'),
	form.Dropdown('Ano', 
				  range(1900, 2014),
				  class_='form-control'),
	form.Textarea('Direccion',
				  form.notnull,
				  class_='form-control'),
	form.Password('Contrasena',
				  form.regexp('[\d\w]{7,}',"Ha de tener al menos 7 caracteres"),
				  class_='form-control'),
	form.Password('Contrasena2',
				  class_='form-control',
				  description = 'Repite contrasena'),
	form.Radio('Pago', ['Efectivo', 'VISA'],
			   class_='radio-inline'),
	form.Textbox('Visa',
				 form.regexp('([0-9]{4}[\s-]){3}[0-9]{4}', 'La tarjeta ha de ser XXXX-XXXX-XXXX-XXXX con guiones o con espacios'),
				 class_='form-control',
				 description = "Numero de tarjeta VISA"),
	form.Checkbox('Acepta las condiciones y privacidad de datos', 
				  form.Validator("No has aceptado las condiciones", lambda i: i == 'true'), 
				  value='true'),
	validators=[form.Validator('Las contrasenas han de ser iguales.', lambda i: i.Contrasena == i.Contrasena2)])

def insertarDatosForm(data):
	conDatos = form.Form(
		form.Textbox('Nombre', 
					 form.notnull,
					 class_='form-control',
					 value=str(data["nombre"])),
		form.Textbox('Apellidos',
					 form.notnull,
					 class_='form-control',
					 value=str(data["apellidos"])),
		form.Textbox('Email',
					 form.notnull,
					 form.regexp('[^@]+@[^@]+\.[^@]+', 'Debe se ser un email'),
					 class_='form-control',
					 value=str(data["email"])),
		form.Dropdown('Dia', 
					  range(1, 31),
					  class_='form-control',
					  value=int(data["dia"])),
		form.Dropdown('Mes', 
					  range(1, 12),
					  class_='form-control',
					  value=int(data["mes"])),
		form.Dropdown('Ano', 
					  range(1900, 2014),
					  class_='form-control',
					  value=int(data["ano"])),
		form.Textarea('Direccion',
					  form.notnull,
					  class_='form-control',
					  value=str(data["direccion"])),
		form.Password('Contrasena',
					  form.regexp('[\d\w]{7,}',"Ha de tener al menos 7 caracteres"),
					  class_='form-control'),
		form.Password('Contrasena2',
					  class_='form-control',
					  description="Repite contrasena: "),
		form.Radio('Pago', ['Efectivo', 'VISA'],
				   class_='radio-inline',
				   checked=str(data["pago"])),
		form.Textbox('Visa',
					 form.regexp('([0-9]{4}[\s-]){3}[0-9]{4}', 'La tarjeta ha de ser XXXX-XXXX-XXXX-XXXX con guiones o con espacios'),
					 class_='form-control',
					 description="Numero de tarjeta VISA: ",
					 value=str(data["visa"])),
		validators=[form.Validator('Las contrasenas han de ser iguales.', lambda i: i.Contrasena == i['Repite contrasena'])])
	
	return conDatos


mensaje = ",  Bienvenido.  <a href='/salir'>Salir</a>" 
contentbody= "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero, adarga antigua, rocin flaco y galgo corredor."


def insertarDatosBD(datos):
	miDB = anydbm.open('miDatabase', 'c')
	miDB["nombre"] = str(datos.Nombre)
	miDB["apellidos"] = str(datos.Apellidos)
	miDB["email"] = str(datos.Email)
	miDB["dia"] = str(datos.Dia)
	miDB["mes"] = str(datos.Mes)
	miDB["ano"] = str(datos.Ano)
	miDB["direccion"] = str(datos.Direccion)
	miDB["contrasena"] = str(datos.Contrasena)
	miDB["contrasena2"] = str(datos.Contrasena2)
	miDB["pago"] = str(datos.Pago)
	miDB["visa"] = str(datos.Visa)	
	miDB.close()
	
def vaciarBD():
	miDB= anydbm.open('miDatabase', 'r')
	for k, v in miDB.iteritems():
		datos[k] = ""
	miDB.close()


# https://docs.python.org/2/library/anydbm.html Doc anydbm
def leerDatosBD(id):
	data = {}
	conn = MongoClient('mongodb://localhost:27017/')
	db = conn.app.usuarios
	items = db.find_one({"_id": id})
	conn.close()

	return items


class index:
	paginaActual = "Inicio"
	def GET(self):
		if 'user' not in session:
			loginForm = login() 
			registroForm = FormularioRegistro()
			return makos.mako_template(varDep = "", titulo = self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), formRegistro = registro, content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		registroForm = FormularioRegistro()
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
			loginForm=login()
			registroForm = FormularioRegistro()
			return makos.mako_template(varDep = "",titulo =self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		registroForm = FormularioRegistro()
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
			loginForm =login()
			registroForm = FormularioRegistro()
			return makos.mako_template(varDep = "",titulo =self.paginaActual, form = loginForm )
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		registroForm = FormularioRegistro()
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
			loginForm = login() 
			registroForm = FormularioRegistro()
			return makos.mako_template(varDep = "",titulo =self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		registroForm = FormularioRegistro()
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
			loginForm = login()
			registroForm = FormularioRegistro()
			return makos.mako_template(varDep = "",titulo =self.paginaActual, form = loginForm)
		else:
			insertarUltimaPagina(self.paginaActual)
			return makos.mako_template(varDep = "",titulo = self.paginaActual, ultimas = mostrarUltimas(), content = contentbody, mensaje = (session.user) + mensaje)

	def POST(self):
		loginForm = login()
		registroForm = FormularioRegistro()
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

class Registro:
	paginaActual = "Registro"
	def GET(self):
		registroForm = FormularioRegistro()
		return makos.mako_template(varDep = "", titulo = self.paginaActual, formRegistro = registroForm)
	
	def POST(self):
		registroForm = FormularioRegistro()
		if not registroForm.validates():
			return makos.mako_template(varDep = "",titulo = self.paginaActual, formRegistro = registroForm )
		else:
			datos = web.input()
			conn = MongoClient('mongodb://localhost:27017')
			db = conn.app.usuarios
			aux = web.input()

			db_usuarios = {
				"nombre": aux.Nombre,
				"apellidos": aux.Apellidos,
				"email": aux.Email,
				"visa": aux.Visa,
				"dia": aux.Dia,
				"mes": aux.Mes,
				"ano": aux.Ano,
				"direccion": aux.Direccion,
				"contrasena": aux.Contrasena,
				"contrasena2": aux.Contrasena2,
				"pago": aux.Pago,
			}

			db.insert(db_usuarios)

			#Cerramos la conexión
			conn.close()
			datos = leerDatosBD()
			registroForm = insertarDatosForm(datos)
			web.debug(datos)
			contenido = imprimirDatosBD()
			return makos.mako_template(varDep = "", titulo = self.paginaActual, formRegistro = registroForm ,mensaje = "Registro exitoso", content = contenido)

			
class cerrarSesion:
	def GET(self):
		session.kill()
		raise web.seeother('/')

if __name__=="__main__":
	web.internalerror = web.debugerror
	app.run()
