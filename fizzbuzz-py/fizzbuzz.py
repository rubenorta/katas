import operator
import re

class Fizzbuzz:

  def divisible_3(self, numero):
    return operator.mod(numero, 3) == 0

  def contiene_3(self, numero):
    return str(numero).count('3') != 0

  def divisible_5(self, numero):
    return operator.mod(numero, 5) == 0

  def contiene_5(self, numero):
    return str(numero).count('5') != 0


  def imprime(self, numero):

    value = ""
    if self.divisible_3(numero) and self.divisible_5(numero):
      value = "fizzbuzz"
    elif self.divisible_3(numero) or self.contiene_3(numero):
      value = "fizz"
    elif self.divisible_5(numero) or self.contiene_5(numero):
      value = "buzz"
    else:
      value = str(numero)

    return value


