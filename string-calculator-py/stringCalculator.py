import re

class Separador:
    separador = ''

class SeparadorSimple(Separador):
    def extrae_separador(self, cadena):
        return ','

class SeparadorConfigurable(Separador):
    def extrae_separador(self, cadena):
        return cadena[2:3]

class SeparadorConfigurableGrande(Separador):
    def extrae_separador(self, cadena):
        return re.findall(r'\/\/\[(.*)\]',cadena)[0]

class SeparadorConfigurableMultiple(Separador):
    def extrae_separador(self, cadena):
        return re.findall(r'^\/\/\[(.*)\]\[(.*)\]\n',cadena)[0]

class Extractor:
    alt_separador = '\n'

class ExtractorSimple(Extractor):
    def dame_digitos(self, cadena, separador):
        cadena_nueva = cadena.replace(self.alt_separador, separador)
        return cadena_nueva.rsplit(separador) 

class ExtractorConfigurable(Extractor):
    def dame_digitos(self, cadena, separador):
        separador_y_cadena = cadena.split(self.alt_separador)   
        cadena_nueva = separador_y_cadena[1]
        return cadena_nueva.rsplit(separador)

class ExtractorMultiple(Extractor):
    def dame_digitos(self, cadena, separadores):
        separador = separadores[0]
        multi_separador = separadores[1]
        separador_y_cadena = cadena.split(self.alt_separador)   
        cadena_nueva = separador_y_cadena[1]
        cadena_nueva = cadena_nueva.replace(multi_separador,separador)
        return cadena_nueva.rsplit(separador)

class Calculadora:
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
    def configura_separador(self):
        self.separador = SeparadorSimple().extrae_separador(self.cadena)
    def extrae_digitos(self):
        return ExtractorSimple().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurable(Calculadora):
    def configura_separador(self):
        self.separador = SeparadorConfigurable().extrae_separador(self.cadena)
    def extrae_digitos(self):
        return ExtractorConfigurable().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurableGrande(Calculadora):
    def configura_separador(self):
        self.separador = SeparadorConfigurableGrande().extrae_separador(self.cadena)
    def extrae_digitos(self):
        return ExtractorConfigurable().dame_digitos(self.cadena, self.separador)

class CalculadoraConfigurableMultiple(Calculadora):
    def configura_separador(self):
        self.separador = SeparadorConfigurableMultiple().extrae_separador(self.cadena)
    def extrae_digitos(self):
        return ExtractorMultiple().dame_digitos(self.cadena, self.separador)

class CalculadoraDeCadenas:

    def es_configurable(self, cadena):
        return re.match(r'//.*\n',cadena)

    def es_grande(self, cadena):
        return re.match(r'^\/\/\[.*\]\n', cadena)

    def es_multiple(self, cadena):
        return re.match(r'^\/\/\[.*\]\[.*\]\n',cadena)

    def factory(self, cadena):
        self.cadena = cadena
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