import web
from web import form

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
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
    form.Dropdown('ano', 
                  range(1900, 2014),
                  class_='form-control'),
    form.Textarea('Direccion',
                  form.notnull,
                  class_='form-control'),
    form.Password('Contrasena',
                  form.regexp('[\d\w]{7,}',"Ha de tener al menos 7 caracteres"),
                  class_='form-control'),
    form.Password('Repite contrasena',
                  class_='form-control'),
    form.Radio('Forma de Pago', ['Efectivo', 'VISA'],
               class_='radio-inline'),
    form.Textbox('Numero de tarjeta VISA',
                 form.regexp('([0-9]{4}[\s-]){3}[0-9]{4}', 'La tarjeta ha de ser XXXX-XXXX-XXXX-XXXX con guiones o con espacios'),
                 class_='form-control'),
    form.Checkbox('Acepta las condiciones y privacidad de datos', 
                  form.Validator("No has aceptado las condiciones", lambda i: i == 'true'), 
                  value='true'),
    validators=[form.Validator('Las contrasenas han de ser iguales.', lambda i: i.Contrasena == i['Repite contrasena'])])


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

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
