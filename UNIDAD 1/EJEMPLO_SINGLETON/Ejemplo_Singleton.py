# coding=utf-8
from random import choice,randrange
class EjemploSingleton(object):

    __instance = None
    nombre =None

    def __str__(self):
        return  "(objeto1 en uso)" + self.nombre


    def __new__(cls):
        if EjemploSingleton.__instance is None:
            EjemploSingleton.__instance=object.__new__(cls)
        return EjemploSingleton.__instance

carlos= EjemploSingleton()
carlos.nombre ="castilleja"
print(carlos)
leslie= EjemploSingleton()
leslie.nombre ="olvera"
print(leslie)
wasnot= EjemploSingleton()
wasnot.nombre ="daniel"
print(wasnot)
was= EjemploSingleton()
was.nombre ="carlos"
print(was)
