


class Contador():

    inicio = 0
    def __init__(self,inicial=0,incremento=1,limite=0):
       self.__inicial = inicial
       self.__incremento = incremento
       self.__limite = limite
       self.__count = inicial

    def get_inicial(self):
        return self.__inicial
    def get_incremento(self):
        return self.__incremento
    def get_limite(self):
        return self.__limite

    def incremento(self):
        if self.count < self.incremento:
            self.count = self.count + self.inicial

            if self.count >= self.limite:
                self.count = self.inicial
                return self.count
        else:

            self.count = self.inicial

        return self.count

    def reiniciar (self):
        self.count = self.inicial

        return self.count

    def getContador(self):
        return self.count
