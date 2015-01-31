import web
from web import form
from pymongo import MongoClient
import ast

client = MongoClient('localhost', 27017)
db = client['DAI-Graficos']

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
	form.Textbox('nombre',
				description='Nombre de la serie',
				class_='form-control'),
	form.Textbox('x',
				description='Punto X',
				 class_='form-control'),
	form.Textbox('y',
				description='Punto Y',
				 class_='form-control')
				)
				
class Punto:
	nombre = ""
	x=0
	y=0
	
	def __init__(self, nombre, x, y):
		self.nombre = nombre
		self.x = x
		self.y = y
		
	def getNombre(self):
		return self.nombre
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def setNombre(self,nombre):
		self.nombre = nombre
		
	def setX(self,x):
		self.x = x
	
	def setY(self,y):
		self.y = y
	
	def getDic(self):
		dic = {"nombre": self.getNombre(),
				"x": self.getX(),
				"y": self.getY()
				}
		return dic
class index:
	"""
		Inserta una serie en la basde de datos con el formato 
			{"nombre": <string>nombre,
			"serie": [<int>,<int>,<int>,...]}
		@param nombre String del nombre
		@param numeroSerie Lista de int que forman la serie
	"""
	def insertarPunto(self, punto):
		punto = punto.getDic()
		puntosCol = db.puntos
		print ("Insertado el punto" + str(punto))
		return puntosCol.insert(punto)
	
	def getPuntosAll(self):
		puntos = db.puntos.find()
		puntosLista = []
		for punto in puntos:
			puntosLista.append({"nombre" : punto["nombre"],"x" : punto["x"],"y" : punto["y"]})
		print(str(puntosLista))
		return puntosLista;	
	
	def selectPunto(self,id):
		cursor = db.puntos.find_one({"_id":str(id)})
		punto = Punto(cursor["nombre"],cursor["x"],cursor["y"])
		return punto
	
	def borrarPuntos(self):
		db.series.remove()
		
	def GET(self):
			
		form = myform()
		# make sure you create a copy of the form by calling it (line above)
		# Otherwise changes will appear globally
		punto = {"x":"null", "y":"null", "nombre":""}
		self.getPuntosAll()
		return render.mapa(form, punto)

	def POST(self):
 		form = myform()
		form.validates()
		
		nombre = str(form["nombre"].value)
		x = ast.literal_eval(form["x"].value)
		y = ast.literal_eval(form["y"].value)
		
		punto = Punto(nombre,x,y)
		idPunto = self.insertarPunto(punto)
		
		puntosAll = self.getPuntosAll();
		return render.mapa(form, puntosAll)
	
if __name__ == "__main__":
	web.internalerror = web.debugerror
	app.run()
