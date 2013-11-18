class Roma():


  caracteres = {}

  def __init__(self):
    self.caracteres = { 'I' : 0  , 'V' : 0 , 'X' : 0 , 'L' : 0 , 'C' : 0 , 'D' : 0 , 'M' : 0}

    self.digito_que_resta = { 'V' : 'I' , 'X' : 'I' , 'L' : 'X' , 'C' : 'X' , 'D' : 'C' , 'M' : 'C'}


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

  def transforma(self, cadena):

    for c in cadena:
      self.incremento(c)
      if not self.es_caracter(c, 'I'):
        if self.hay(self.digito_que_resta[c]):
          self.resta_caracter(self.digito_que_resta[c])

    if self.mas_caracteres_permitidos():
      raise RuntimeError

    return  self.suma_caracteres()
