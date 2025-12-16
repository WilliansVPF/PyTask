import task
import repository

continua = True
rep = repository.Repository()

def listarMenu():
    print("\n--- MENU DE TAREFAS ---")
    print("1 - Cadastrar Nova Tarefa")
    print("2 - Edita Tarefa")
    print("3 - Finalizar Tarefa")
    print("4 - Excluir Tarefa")
    print("5 - Listar Tarefas")
    print("6 - Detalhes da Tarefas")
    print("0 - Sair")
    print("-----------------------")

while (continua):

    listarMenu()

    opcao = int(input("Digite uma Opção: "))
    if opcao == 1:
        titulo = input("Digite um titulo: ")
        descricao = input("Digite uma descrição: ")
        tarefa = task.Task(titulo,descricao)
        rep.cadastrarTask(tarefa)
    elif opcao == 2:
        id = int(input("Digite o Id da tarefa: "))
        task = rep.findTaskById(id)
        if task == None:
            print("Tarefa não encontrada")
        else:
            task.titulo = input("Digite um titulo: ")
            task.descricao = input("Digite uma descrição: ")
            rep.editaTarefa(id, task)
    elif opcao == 3:
        id = input("Digite o ID: ")
        rep.finalizarTarefa(int(id))
    elif opcao == 4:
        id = input("Digite o ID: ")
        rep.deletaTask(int(id))
    elif opcao == 5:
        rep.listaTarefa()
    elif opcao == 6:
        id = input("Digite o ID: ")
        rep.detalheTarefa(int(id))
    elif opcao == 0:
        print("Programa Encerrado")
        continua = False
    else:
        print("\n###Digite uma opção valida###")



# rep = repository.Repository()
# for i in range(0,3):
#     tarefa = task.Task("Tarefa " + str(i), "tarefa de teste " + str(i))
#     # tarefa.id = int(i)
#     rep.cadastrarTask(tarefa)
#
# rep.listaTarefa()

# id = rep.ultimoId()
# print(id)
