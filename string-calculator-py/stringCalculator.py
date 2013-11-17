from calculadora import FactoriaCalculadora

class StringCalculator:

    def add(self, cadena):
        calculadora = FactoriaCalculadora().dame_calculadora(cadena)
        calculadora.configura_separador()
        return calculadora.suma_digitos(calculadora.extrae_digitos())
