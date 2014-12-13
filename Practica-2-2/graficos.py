import web
from web import form
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['DAI-Graficos']

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
	form.Textbox('nombre',
				description='Nombre de la serie',
				class_='form-control'),
	form.Textbox('serie',
				description='Valores de la serie separados por comas',
				 class_='form-control')
				)

class index:
	"""
		Inserta una serie en la basde de datos con el formato 
			{"nombre": <string>nombre,
			"serie": [<int>,<int>,<int>,...]}
		@param nombre String del nombre
		@param numeroSerie Lista de int que forman la serie
	"""
	def insertarSerie(self, nombre, numerosSerie):
		serie = {"nombre": nombre,
				"serie": numerosSerie}
		seriesCol = db.series
		print ("Insertada la serie" + str(serie))
		return seriesCol.insert(serie)
	
	def getSerieAll(self):
		series = db.series.find()
		seriesLista = []
		for serie in series:
			seriesLista.append({"data" : serie["serie"],"name" : str(serie["nombre"])})
		return seriesLista;	
	
	def borrarSeries(self):
		db.series.remove()
		
	def GET(self):
			
		form = myform()
		# make sure you create a copy of the form by calling it (line above)
		# Otherwise changes will appear globally
		seriesLista = self.getSerieAll();
		return render.grafico(form, seriesLista)

	def POST(self):
 		form = myform()
		form.validates()
		
		nombre = str(form["nombre"].value);
		numerosSerie=str(form["serie"].value);
		numerosSerie = [int(x) for x in numerosSerie.split(',')]
		
		self.insertarSerie(nombre,numerosSerie)
		seriesLista = self.getSerieAll();
		
		return render.grafico(form, seriesLista)
	
	
if __name__ == "__main__":
	web.internalerror = web.debugerror
	app.run()
