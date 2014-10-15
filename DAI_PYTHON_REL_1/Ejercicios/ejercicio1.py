# -*- coding: utf-8 -*-

import random

print "Introduzca un numero del 1 al 100";
num_rand=random.randint(1, 100);
num_in = input();
while(num_in != num_rand):
	if(num_in < num_rand):
		print"El numero introducido es menor";
	else:
		print "El numero introducido es mayor";
	num_in = input();
print "¡Enhorabuena! ¡Has acertado!";