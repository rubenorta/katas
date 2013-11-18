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

  def test_transforma_XI(self):
    self.assertEquals(self.r.transforma("XI"), 11)

  def test_transforma_XX(self):
    self.assertEquals(self.r.transforma("XX"), 20)

  def test_transforma_XXXI(self):
    self.assertEquals(self.r.transforma("XXXI"), 31)

  def test_transforma_XXIV(self):
    self.assertEquals(self.r.transforma("XXIV"), 24)

  def test_transforma_L(self):
    self.assertEquals(self.r.transforma("L"), 50)

  def test_transforma_XL(self):
    self.assertEquals(self.r.transforma("XL"), 40)

  def test_transforma_LX(self):
    self.assertEquals(self.r.transforma("LX"), 60)

  def test_transforma_C(self):
    self.assertEquals(self.r.transforma("C"), 100)

  def test_transforma_XC(self):
    self.assertEquals(self.r.transforma("XC"), 90)

  def test_transforma_CCCLXIX(self):
    self.assertEquals(self.r.transforma("CCCLXIX"), 369)

  def test_transforma_D(self):
    self.assertEquals(self.r.transforma("D"), 500)

  def test_transforma_CD(self):
    self.assertEquals(self.r.transforma("CD"), 400)

  def test_transforma_CDXLVIII(self):
    self.assertEquals(self.r.transforma("CDXLVIII"), 448)

  def test_transforma_M(self):
    self.assertEquals(self.r.transforma("M"), 1000)

  def test_transforma_MCMXCVIII(self):
    self.assertEquals(self.r.transforma("MCMXCVIII"), 1998)

  def test_transforma_MMDCCLI(self):
    self.assertEquals(self.r.transforma("MMDCCLI"), 2751)
