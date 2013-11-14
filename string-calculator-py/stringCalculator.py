from calculadora import CalculadoraDeCadenas

class StringCalculator:

    def add(self, cadena):
        calculadora = CalculadoraDeCadenas().factory(cadena)
        calculadora.configura_separador()
        return calculadora.suma_digitos(calculadora.extrae_digitos())
