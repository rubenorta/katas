class Roma():


  caracteres = {}

  def __init__(self):
    self.caracteres = { 'I' : 0  , 'V' : 0 , 'X' : 0 , 'L' : 0 , 'C' : 0 , 'D' : 0 , 'M' : 0}

  def suma_caracteres(self):
    return self.caracteres['I'] + self.caracteres['V']*5 + self.caracteres['X']*10 + self.caracteres['L']*50 + self.caracteres['C']*100 + self.caracteres['D']*500 + self.caracteres['M']*1000

  def es_caracter(self, caracterA, caracterB):
    return caracterA == caracterB

  def incremento(self, caracter):
    self.caracteres[caracter] += 1

  def resta_caracter(self, caracter):
    self.caracteres[caracter] = -1 * self.caracteres[caracter]

  def hay(self, caracter):
    return self.caracteres[caracter] > 0

  def mas_caracteres_permitidos(self):
    for caracter in self.caracteres.keys():
      if self.caracteres[caracter] > 3:
        return True
    return False


  def existen_mas_I_permitidas(self):
    return self.caracteres['I'] > 3

  def transforma(self, cadena):

    for c in cadena:

      if self.es_caracter(c, 'I'):
        self.incremento('I')

      if self.es_caracter(c, 'V'):
        self.incremento('V')
        if self.hay('I'):
          self.resta_caracter('I')

      if self.es_caracter(c, 'X'):
        self.incremento('X')
        if self.hay('I'):
          self.resta_caracter('I')

      if self.es_caracter(c, 'L'):
        self.incremento('L')
        if self.hay('X'):
          self.resta_caracter('X')

      if self.es_caracter(c, 'C'):
        self.incremento('C')
        if self.hay('X'):
          self.resta_caracter('X')

      if self.es_caracter(c, 'D'):
        self.incremento('D')
        if self.hay('C'):
          self.resta_caracter('C')

      if self.es_caracter(c, 'M'):
        self.incremento('M')
        if self.hay('C'):
          self.resta_caracter('C')


    if self.mas_caracteres_permitidos():
      raise RuntimeError

    return  self.suma_caracteres()
