class Materia:
    def __init__(self, nome="", id=0, sigla="", descricao=""):
        self.__nome = nome
        self.__id = id
        self.__descricao = descricao
        self.__sigla = sigla

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo):
        self.__nome = novo

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo):
        self.__id = novo

    @property
    def sigla(self):
        return self.__sigla
    @sigla.setter
    def sigla(self, novo):
        self.__sigla = novo

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, novo):
        self.__descricao = novo