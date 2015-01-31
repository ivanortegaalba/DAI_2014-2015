import web

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

class index:
	
	def GET(self):
			
		return render.tweets()

if __name__ == "__main__":
	web.internalerror = web.debugerror
	app.run()
