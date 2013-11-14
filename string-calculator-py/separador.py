import re

class Separador(object):
    """Separador"""
    separador = ''

    def __init__ (self):
        pass

    def extrae_separador(self, cadena):
        """Extrae el separador de una cadena"""
        pass

class SeparadorSimple(Separador):
    """Separador Simple"""
    def extrae_separador(self, cadena):
        """Extrae el separador de una cadena para calculadoras simples"""
        return ','

class SeparadorConfigurable(Separador):
    """Separador Configurable"""
    def extrae_separador(self, cadena):
        """Extrae el separador de una cadena para calculadoras configurables"""
        return cadena[2:3]

class SeparadorConfigurableGrande(Separador):
    """Separador Configurable Grande"""
    def extrae_separador(self, cadena):
        """Extrae el separador de una cadena para calculadoras configurables grandes"""
        return re.findall(r'\/\/\[(.*)\]', cadena)[0]

class SeparadorConfigurableMultiple(Separador):
    """Separador Configurable Multiple"""
    def extrae_separador(self, cadena):
        """Extrae el separador de una cadena para calculadoras configurables multiples"""
        return re.findall(r'^\/\/\[(.*)\]\[(.*)\]\n', cadena)[0]
