'''
Created on 2/12/2014

@author: ivanortegaalba
'''
# -*- coding: utf-8 -*-

from lxml import etree

tree = etree.parse('portada.xml')

rss = tree.getroot() # elemento raiz

# Los elementos funcionan como listas
channel = rss[0]     # Primer hijo

for e in  channel:
	if (e.tag == 'item'):  # Atributo tag, nobre del elemento
		# Anado <item modificado="hoy">
		e.set('modificado', 'hoy')		
		
		# Los atributos del xml funcionan casi como diccionarios		
		print (e.keys(), e.get('modificado'))		
		
		# Creo otro elemento
		otro = etree.Element('otro')   # <otro></otro>
		
		# Atributo text
		otro.text = 'Texto de otro'
		e.insert(0, otro) # Anado <otro>Texto de otro</otro>

print (etree.tounicode(rss, pretty_print=True))