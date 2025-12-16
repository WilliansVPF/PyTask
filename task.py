from datetime import date

class Task():

    def __init__(self, titulo = None, descricao = None):
        self.__id = None
        self.__titulo = titulo
        self.__descricao = descricao
        self.__dataCriacao = date.today()
        self.__dataConclusao = None
        self.__status = 0

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def dataCriacao(self):
        return self.__dataCriacao

    @property
    def dataConclusao(self):
        return self.__dataConclusao

    @property
    def status(self):
        return self.__status

    def finalizaTarefa(self):
        self.__status = 1
        self.__dataConclusao = date.today()