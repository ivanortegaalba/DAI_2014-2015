# -*- coding: utf-8 -*-
"""Ordena matrices unidimensionales aleatorias en funcion a un algoritmo elegido"""

import random;

def randomMatrix(n): #Crea un vector de n elementos aleatorios
    random_vector = [];
    for i in range(n):
        random_vector.append(random.randint(0,100));
        #print "vector["+str(i)+"]="+str(random_vector[i]);
    return random_vector;

def Burbuja(v):
    for izq in range(len(v)-1, 0, -1):
        for index in range(izq):
            if v[index] > v[index + 1]:
                v[index], v[index + 1] = v[index + 1], v[index];
    return v;

def QuickShort(v):
    if v == []: 
        return []
    else:
        pivot = v[0]
        lesser = QuickShort([x for x in v[1:] if x < pivot])
        greater = QuickShort([x for x in v[1:] if x >= pivot])
        return lesser + [pivot] + greater
    return v;

def Voraz(v):
    for i in v:
        for j in range(len(v)-1):
            if v[j] > v[j+1]:
                t = v[j];
                v[j]=v[j+1];
                v[j+1] = t;
    return v;

"""una forma elegante de hacer un switch/case en python, 
puede hacerse porque las funciones tiene el mismo parámetro."""
options = {
           1: QuickShort,
           2: Burbuja,
           3: Voraz
};


print "Introduce la dimension de la matriz:";
n = input();

print "Introduce el método a ordenar:\n 1. QuickShort \n 2.Burbuja \n3.Algoritmo voraz";
ordenation_type=input();



v = randomMatrix(n);

print options[ordenation_type](v);
