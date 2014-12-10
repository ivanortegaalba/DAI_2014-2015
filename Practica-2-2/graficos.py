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
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            numerosSerie=str(form['serie'].value);
            numerosSerie = [int(x) for x in numerosSerie.split(',')]
            print numerosSerie
            serie = {"nombre": form['nombre'].value,
					"serie": numerosSerie}
            series = db.series
            idSerie = series.insert(serie);
            
            if(idSerie):
            	serieBD = series.find_one({'_id': idSerie})
            	return str(serieBD["serie"])
            else:
            	return "Los valores no han sido guardados"

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
