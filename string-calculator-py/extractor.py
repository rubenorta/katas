class Extractor(object):
    """Extractor"""
    alt_separador = '\n'
    def __init__ (self):
        pass

    def dame_digitos(self, cadena, separador):
        """Devuelve los digitos de la cadena utilizando separador como separador"""
        pass

class ExtractorSimple(Extractor):
    """Extractor Simple"""
    def dame_digitos(self, cadena, separador):
        """Dame digitos teniendo en cuenta un extractor simple"""
        cadena_nueva = cadena.replace(self.alt_separador, separador)
        return cadena_nueva.rsplit(separador)

class ExtractorConfigurable(Extractor):
    """Dame digitos teniendo en cuenta un extractor configurable"""
    def dame_digitos(self, cadena, separador):
        separador_y_cadena = cadena.split(self.alt_separador)
        cadena_nueva = separador_y_cadena[1]
        return cadena_nueva.rsplit(separador)

class ExtractorMultiple(Extractor):
    """Dame digitos teniendo en cuenta un extractor multiple"""
    def dame_digitos(self, cadena, separadores):
        separador = separadores[0]
        multi_separador = separadores[1]
        separador_y_cadena = cadena.split(self.alt_separador)
        cadena_nueva = separador_y_cadena[1]
        cadena_nueva = cadena_nueva.replace(multi_separador, separador)
        return cadena_nueva.rsplit(separador)
