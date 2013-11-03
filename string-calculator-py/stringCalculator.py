import re

class SeparadorSimple:
    def dame_separador(self, cadena):
        return ','

class SeparadorConfigurable:
    def dame_separador(self, cadena):
        return cadena[2:3]

class SeparadorConfigurableGrande:
    def dame_separador(self, cadena):
        return re.findall(r'\/\/\[(.*)\]',cadena)[0]

class SeparadorConfigurableMultiple:
    def dame_separador(self, cadena):
        return re.findall(r'^\/\/\[(.*)\]\[(.*)\]\n',cadena)[0]

class ExtractorSimple:
    def dame_digitos(self, cadena, separador):
        cadena_nueva = cadena.replace('\n', separador)
        return cadena_nueva.rsplit(separador)

class ExtractorConfigurable:
    def dame_digitos(self, cadena, separador):
        separador_y_cadena = cadena.split('\n')   
        cadena_nueva = separador_y_cadena[1]
        return cadena_nueva.rsplit(separador)

class ExtractorMultiple:
    def dame_digitos(self, cadena, separador, multi_separador):
        separador_y_cadena = cadena.split('\n')   
        cadena_nueva = separador_y_cadena[1]
        cadena_nueva = cadena_nueva.replace(multi_separador,separador)
        return cadena_nueva.rsplit(separador)

class StringCalculator:

    separador = ','
    multi_separador = ''

    def contiene_separador_configurable(self, cadena):
        return cadena.find('//') == 0

    def contiene_separador_grande(self, cadena):
        return cadena.find('//[') == 0

    def contiene_separador_multiple(self, cadena):
        return re.match(r'^\/\/\[.*\]\[.*\]\n',cadena)


    def extrae_digitos(self, cadena):

        elementos_suma = []
        if self.contiene_separador_multiple(cadena):
            elementos_suma = ExtractorMultiple().dame_digitos(cadena, self.separador, self.multi_separador)
        elif self.contiene_separador_configurable(cadena):
            elementos_suma = ExtractorConfigurable().dame_digitos(cadena, self.separador)
        else:
            elementos_suma = ExtractorSimple().dame_digitos(cadena, self.separador)
        return elementos_suma 

    def suma_digitos(self, digitos):
        total = 0
        valores_negativos = ""
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

    def add(self, cadena):
        if not cadena:
            return 0
        else:
            self.configura_separador(cadena)
            digitos = self.extrae_digitos(cadena)
            return self.suma_digitos(digitos)


    def configura_separador(self, cadena):
        if self.contiene_separador_configurable(cadena):
            if self.contiene_separador_multiple(cadena):
                separadores = SeparadorConfigurableMultiple().dame_separador(cadena)
                self.separador = separadores[0]
                self.multi_separador = separadores[1]
            elif self.contiene_separador_grande(cadena): 
                self.separador = SeparadorConfigurableGrande().dame_separador(cadena)
            else:    
                self.separador = SeparadorConfigurable().dame_separador(cadena)
        else:
            self.separador = SeparadorSimple().dame_separador(cadena)
