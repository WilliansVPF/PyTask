# import task
from itertools import count


class Repository:

    def __init__(self):
        self.__lista = []


    def cadastrarTask(self, task):
        id = self.__ultimoId()
        task.id = id + 1
        self.__lista.append(task)

    def listaTarefa(self):
        print("\n###Lista de Tarefas###")
        for i in self.__lista:
            status = "Incompleta" if i.status == 0 else "Completa"
            print(f"Id: {i.id} Titulo: {i.titulo} // Descrição: {i.descricao} // Status: {status}")

    def detalheTarefa(self, id):
        task = self.findTaskById(id)
        if task:
            status = "Incompleta" if task.status == 0 else "Completa"
            print("\n###Detalhes da Tarefa###")
            print(f"Id: {task.id} \nTitulo: {task.titulo} \nDescrição: {task.descricao} \nData de criação: {task.dataCriacao} \nStatus: {status} \nData de conclusão: {task.dataConclusao}")
        else:
            print("Tarefa não encontrada")

    def finalizarTarefa(self, id):
        task = next((obj for obj in self.__lista if obj.id == id), None)
        if task:
            task.finalizaTarefa()
        else:
            print("Tarefa não encontrada")
            return None

        i = self.__indiceTarefa(id)
        self.__lista[i] = task

    def editaTarefa(self, id, taskEditada):
        i = self.__indiceTarefa(id)
        self.__lista[i] = taskEditada

    def findTaskById(self, id):
        task = next((obj for obj in self.__lista if obj.id == id), None)
        return task

    def deletaTask(self, id):
        i = self.__indiceTarefa(id)
        self.__lista.pop(i)

    def __ultimoId(self):
        i = len(self.__lista)
        if i != 0:
            task = self.__lista[i-1]
            return task.id
        else:
            return 0

    def __indiceTarefa(self, id):
        for index, obj in enumerate(self.__lista):
            if obj.id == id:
                return index
        return None