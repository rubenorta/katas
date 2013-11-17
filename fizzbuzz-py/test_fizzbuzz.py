import unittest
import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

  def setUp(self):
    self.fb = fizzbuzz.Fizzbuzz()

  def test_print_1(self):

    self.assertEquals(self.fb.imprime(1),"1")

  def test_print_2(self):
    self.assertEquals(self.fb.imprime(2),"2")

  def test_print_3(self):
    self.assertEquals(self.fb.imprime(3),"fizz")

  def test_print_5(self):
    self.assertEquals(self.fb.imprime(5), "buzz")

  def test_print_divisible_3(self):
    self.assertEquals(self.fb.imprime(6),"fizz")

  def test_print_divisible_5(self):
    self.assertEquals(self.fb.imprime(10),"buzz")

  def test_print_incluye_3(self):
    self.assertEquals(self.fb.imprime(13), "fizz")

  def test_print_incluye_5(self):
    self.assertEquals(self.fb.imprime(25), "buzz")

  def test_print_divisible_3_y_5(self):
    self.assertEquals(self.fb.imprime(15), "fizzbuzz")

if __name__ == '__main__':
    unittest.main()


