import re
import separador
import extractor

class Calculadora(object):
    """Calculadora"""
    cadena = ''
    separador = ''

    def __init__ (self, cadena):
        self.cadena = cadena

    def suma_digitos(self, digitos):
        total = 0
        valores_negativos = ""

        if not digitos[0]:
            return 0
        for digito in digitos:
            if digito:
                if int(digito) < 0:
                    valores_negativos += digito + " "
                elif int(digito) < 1000:
                    total = total + int(digito)
            else:
                raise RuntimeError

        if valores_negativos:
            mensaje_error = 'Negatives not Allowed ' + valores_negativos
            raise RuntimeError(mensaje_error)
        return total

class CalculadoraSimple(Calculadora):
    """Calculadora Simple"""
    def configura_separador(self):
        """Configura el separador"""
        self.separador = separador.SeparadorSimple().extrae_separador(self.cadena)
    def extrae_digitos(self):
        """Extrae los digitos"""
        return extractor.ExtractorSimple().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurable(Calculadora):
    """Calculadora Configurable"""
    def configura_separador(self):
        """Configura el separador"""
        self.separador = separador.SeparadorConfigurable().extrae_separador(self.cadena)
    def extrae_digitos(self):
        """Extrae los digitos"""
        return extractor.ExtractorConfigurable().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurableGrande(Calculadora):
    """Calculadora Configurable Grande"""
    def configura_separador(self):
        """Configura el separador"""
        self.separador = separador.SeparadorConfigurableGrande().extrae_separador(self.cadena)
    def extrae_digitos(self):
        """Extrae los digitos"""
        return extractor.ExtractorConfigurable().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurableMultiple(Calculadora):
    """Calculadora Configurable Multiple"""
    def configura_separador(self):
        """Configura el separador"""
        self.separador = separador.SeparadorConfigurableMultiple().extrae_separador(self.cadena)
    def extrae_digitos(self):
        """Extrae los digitos"""
        return extractor.ExtractorMultiple().dame_digitos(self.cadena, self.separador)

class CalculadoraDeCadenas(object):
    """Factoria para devolver la calculadora debido a cadena"""

    def es_configurable(self, cadena):
        """Permite saber si la calculadora es del tipo configurable"""
        return re.match(r'//.*\n', cadena)

    def es_grande(self, cadena):
        """Permite saber si la calculadora es configurable grande"""
        return re.match(r'^\/\/\[.*\]\n', cadena)

    def es_multiple(self, cadena):
        """Permite saber si la calculadora es configurable multiple"""
        return re.match(r'^\/\/\[.*\]\[.*\]\n', cadena)

    def factory(self, cadena):

        if self.es_multiple(cadena):
            return CalculadoraConfigurableMultiple(cadena)
        elif self.es_grande(cadena):
            return CalculadoraConfigurableGrande(cadena)
        elif self.es_configurable(cadena):
            return CalculadoraConfigurable(cadena)
        else:
            return CalculadoraSimple(cadena)
