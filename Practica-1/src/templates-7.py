# -*- encoding: utf-8 -*-
import web
from web import form
from web.contrib.template import render_mako

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

makos = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        encoding_errors='replace'
        )

login = form.Form(
    form.Textbox('Usuario', class_="form-control"),
    form.Password('Contrasena', class_="form-control"),
    form.Checkbox('Recuerdame', 
                  form.Validator("No has aceptado las condiciones", lambda i: i == 'true'), 
                  value='true'),
    form.Button('Entrar', _class="button btn-default"))

logout = "<a href='/'>Salir</a>"

contentbody= "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero, adarga antigua, rocin flaco y galgo corredor."
class index:
    def GET(self):
        login_form = login()
        return makos.mako_template(form = login_form, content=contentbody) 

    def POST(self):
        login_form = login()
        if not login_form.validates():
            return makos.mako_template(form = login_form)        
        else:
            return makos.mako_template(message = "Bienvenido %s!  <a class = 'button' href='/'>Salir</a>" % (login_form['Usuario'].value))

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
