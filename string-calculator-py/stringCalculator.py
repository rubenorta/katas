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

class Extractor(object):
    """Extractor"""
    alt_separador = '\n'
    def __init__ (self):
        pass

    def dame_digitos(self, cadena, separador):
        """Devuelve los digitos de la cadena utilizando separador como separador"""
        pass

class ExtractorSimple(Extractor):
    """Extractor Simple"""
    def dame_digitos(self, cadena, separador):
        """Dame digitos teniendo en cuenta un extractor simple"""
        cadena_nueva = cadena.replace(self.alt_separador, separador)
        return cadena_nueva.rsplit(separador)

class ExtractorConfigurable(Extractor):
    """Dame digitos teniendo en cuenta un extractor configurable"""
    def dame_digitos(self, cadena, separador):
        separador_y_cadena = cadena.split(self.alt_separador)
        cadena_nueva = separador_y_cadena[1]
        return cadena_nueva.rsplit(separador)

class ExtractorMultiple(Extractor):
    """Dame digitos teniendo en cuenta un extractor multiple"""
    def dame_digitos(self, cadena, separadores):
        separador = separadores[0]
        multi_separador = separadores[1]
        separador_y_cadena = cadena.split(self.alt_separador)
        cadena_nueva = separador_y_cadena[1]
        cadena_nueva = cadena_nueva.replace(multi_separador, separador)
        return cadena_nueva.rsplit(separador)

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
        self.separador = SeparadorSimple().extrae_separador(self.cadena)
    def extrae_digitos(self):
        """Extrae los digitos"""
        return ExtractorSimple().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurable(Calculadora):
    """Calculadora Configurable"""
    def configura_separador(self):
        """Configura el separador"""
        self.separador = SeparadorConfigurable().extrae_separador(self.cadena)
    def extrae_digitos(self):
        """Extrae los digitos"""
        return ExtractorConfigurable().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurableGrande(Calculadora):
    """Calculadora Configurable Grande"""
    def configura_separador(self):
        """Configura el separador"""
        self.separador = SeparadorConfigurableGrande().extrae_separador(self.cadena)
    def extrae_digitos(self):
        """Extrae los digitos"""
        return ExtractorConfigurable().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurableMultiple(Calculadora):
    """Calculadora Configurable Multiple"""
    def configura_separador(self):
        """Configura el separador"""
        self.separador = SeparadorConfigurableMultiple().extrae_separador(self.cadena)
    def extrae_digitos(self):
        """Extrae los digitos"""
        return ExtractorMultiple().dame_digitos(self.cadena, self.separador)

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

class StringCalculator:

    def add(self, cadena):
        calculadora = CalculadoraDeCadenas().factory(cadena)
        calculadora.configura_separador()
        return calculadora.suma_digitos(calculadora.extrae_digitos())
