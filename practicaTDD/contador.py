


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
        if self.__count < self.__incremento:
            self.__count = self.__count + self.__inicial

            if self.__count >= self.__limite:
                self.__count = self.__inicial
                return self.__count
        else:

            self.__count = self.__inicial

        return self.__count

    def reiniciar (self):
        self.__count = self.__inicial

        return self.__count

    def getContador(self):
        return self.__count
