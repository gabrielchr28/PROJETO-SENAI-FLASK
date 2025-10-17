class Aluno:
    def __init__(self, id=0, nome="", cpf="", idade=0):
        self.__id = id
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

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

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf_n):
        self.__cpf = cpf_n

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade_n):
        self.__idade = idade_n