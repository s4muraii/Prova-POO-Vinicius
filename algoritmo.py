from classes import *
import os

def main():
    while True:
        try:
            menu = int(input("---------------------------------------------Bem-Vindo a TO-DO!--------------------------------------------- \n\nDigite a opção desejada: \n[1] Adicionar tarefas\n[2] Listar tarefas\n[3] Excluir tarefas\n[4] Sair\n\nDigite sua escolha: "))
            os.system("cls")
            try:
                match menu:
                    case 1:
                        add = ToDoList()
                        add.adicionar_tarefa(input("Você escolheu adicionar uma tarefa! Digite a tarefa aqui: "))
                        print(f"Tarefa adicionada!")
                        os.system("pause")
                        os.system("cls")
                        x = 1

                    case 2:
                        if x == 1:
                            print(f"Você escolheu listar as tarefas! As tarefas inseridas são: {add.listar_tarefas()}")
                            os.system("pause")
                            os.system("cls")

                        elif x < 1 or x > 1:
                            print("Você ainda não adicionou nenhuma tarefa!")
                            os.system("pause")
                            os.system("cls")

                        else:
                            print("Opção inválida!")
                            
                    case 3:
                        add.excluir_tarefa(int(f"Você resolveu remover uma tarefa!\n as tarefas cadastradas são: {add.listar_tarefas()}\n\n Qual tarefa deseja remover?: "))

                    case 4:
                        break
            except ValueError as erro:
                print("Opção inválida!")
            
        except ValueError as erro:
            print("Opção inválida!")
