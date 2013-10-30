import unittest
import stringCalculator

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.sc = stringCalculator.StringCalculator()

    def test_cadena_vacia(self):
        self.assertEquals(self.sc.add(""),0)

    def test_cadena_un_digito(self):
        self.assertEquals(self.sc.add("1"),1)

    def test_cadena_dos_digitos(self):
        self.assertEquals(self.sc.add("1,2"),3)

    def test_cadena_multiples_digitos(self):
        self.assertEquals(self.sc.add("1,2,3"),6)

    def test_separador_retorno_y_coma(self):
        self.assertEquals(self.sc.add("1\n2,3"),6)

    def test_dos_separadores_seguidos(self):
        with self.assertRaises(RuntimeError):
            self.sc.add("1\n,2")

    def test_separador_configurable(self):
        self.assertEquals(self.sc.add("//;\n1;2"),3)

    def test_valores_negativos_erroneo(self):
        with self.assertRaises(RuntimeError):
            self.sc.add("//;\n1;-1")

    def test_ignorar_valores_mayores_1000(self):
        self.assertEquals(self.sc.add('1000,2,3'),5)

if __name__ == '__main__':
    unittest.main()