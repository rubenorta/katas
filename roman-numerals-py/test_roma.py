import unittest
import roma

class TestRoma(unittest.TestCase):

  def setUp(self):
    self.r = roma.Roma()

  def test_transforma_I(self):
    self.assertEquals(self.r.transforma('I'),1)

  def test_transforma_II(self):
    self.assertEquals(self.r.transforma('II'),2)

  def test_transforma_III(self):
    self.assertEquals(self.r.transforma('III'),3)

  def test_transforma_IIII(self):
    with self.assertRaises(RuntimeError):
      self.r.transforma("IIII")

  def test_transforma_V(self):
    self.assertEquals(self.r.transforma("V"), 5)

  def test_transforma_IV(self):
    self.assertEquals(self.r.transforma("IV"), 4)

  def test_transforma_VI(self):
    self.assertEquals(self.r.transforma("VI"), 6)

  def test_transforma_VII(self):
    self.assertEquals(self.r.transforma("VII"), 7)

  def test_transforma_VIII(self):
    self.assertEquals(self.r.transforma("VIII"), 8)

  def test_transforma_VIIII(self):
    with self.assertRaises(RuntimeError):
      self.r.transforma("VIIII")

  def test_transforma_X(self):
    self.assertEquals(self.r.transforma("X"), 10)

  def test_transforma_IX(self):
    self.assertEquals(self.r.transforma("IX"), 9)



