import web
from web import form

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox('Nombre'),
    form.Textbox('Email',
        form.notnull,
        form.regexp('[^@]+@[^@]+\.[^@]+', 'Debe se ser un email')),
#        form.Validator('Must be more than 5', lambda x:int(x)>5)),
    form.Textarea('Motivo de contacto'),
    form.Checkbox('Acepta las condiciones y privacidad de datos'),
    form.Dropdown('Urgencia', ['Alta', 'Media', 'Baja']))

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
            return "Pronto contactaremos con usted %s!  Le enviaremos un email a: %s" % (form['Nombre'].value, form['Email'].value)

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
