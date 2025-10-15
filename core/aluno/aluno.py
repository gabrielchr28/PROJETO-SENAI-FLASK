class Aluno:
    def __init__(self, id=0, nome=""):
        self.__id = id
        self.__nome = nome

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id_n):
        self.__id = id_n

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome_n):
        self.__nome = nome_n