import re

class Separador(object):
    separador = ''

    def __init__ (self):
        pass

    def extrae_separador(self, cadena):
        pass

class SeparadorSimple(Separador):
    def extrae_separador(self, cadena):
        return ','

class SeparadorConfigurable(Separador):
    def extrae_separador(self, cadena):
        return cadena[2:3]

class SeparadorConfigurableGrande(Separador):
    def extrae_separador(self, cadena):
        return re.findall(r'\/\/\[(.*)\]', cadena)[0]

class SeparadorConfigurableMultiple(Separador):
    def extrae_separador(self, cadena):
        return re.findall(r'^\/\/\[(.*)\]\[(.*)\]\n', cadena)[0]
