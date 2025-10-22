class Professor:
    def __init__(self, nome="", id=0, formacao=0, idade=0,):
        self.__id = id
        self.__nome = nome
        self.__formacao = formacao
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
    def formacao(self):
        return self.__formacao
    @formacao.setter
    def formacao(self, formacao_n):
        self.__formacao = formacao_n

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade_n):
        self.__idade = idade_n
