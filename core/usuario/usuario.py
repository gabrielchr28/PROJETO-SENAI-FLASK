class Usuario:
    def __init__(self, nome_usu="", senha=0, ativo=0, id=0):
        self.__usuario = nome_usu
        self.__senha = senha
        self.__ativo = ativo
        self.__id = id

    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, usu_n):
        self.__usuario = usu_n

    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha_n):
        self.__senha = senha_n

    @property
    def ativo(self):
        return self.__ativo
    @ativo.setter
    def ativo(self):
        self.__ativo = not self.__ativo

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id_n):
        self.__id = id_n