'''
Created on 2/12/2014

@author: ivanortegaalba
'''
# -*- coding: iso-8859-15
# etree sax parser
from lxml import etree
import sys

#===============================================================================
# if len(sys.argv) >= 2:
# 	print "La cadena introducida tiene",len(sys.argv[1]),"caracteres";
#===============================================================================
    
class ParseRssNews ():
	noticias = 0;
	imagenes = 0;
	def __init__ (self):
		print('Principio del archivo------------------------')
				
	def start (self, tag, attrib):  # Etiquetas de inicio
		if(attrib['type'] == 'image'):
			self.imagenes = self.imagenes + 1
		for k in attrib:
			print (' %s =" %s"' % (k, attrib[k]))
			 	
	def end (self, tag):  # Etiquetas de fin
		if (tag == 'item'):
			self.noticias = self.noticias + 1;

 	#==========================================================================
 	# def data (self, data):  # texto)
		# print(data)
		#==========================================================================
	def close (self):
		print('HEMOS ENCONTRADO: ' + str(self.noticias) + ' NOTICIAS')
		print ('HEMOS ENCONTRADO: ' + str(self.imagenes) + ' IMAGENES') 
		print (' - - - -Fin del archivo')

parser = etree.XMLParser (target=ParseRssNews ())
etree.parse ('portada.xml', parser)
#===============================================================================
# else:
# 	print "Este programa necesita un parametro";
#===============================================================================
#'portada.xml' es un rss en
# http://ep00.epimg.net/rss/elpais/portada.xml