from calculadora import Calculadora

class StringCalculator:

    def add(self, cadena):
        calculadora = Calculadora(cadena)
        calculadora.configura_separador()
        return calculadora.suma_digitos(calculadora.extrae_digitos())
