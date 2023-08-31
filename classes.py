tarefas = {}

class ToDoList:
    def adicionar_tarefa(self, descricao: str):
        self.descricao = descricao
        descricao.append(tarefas)
        return descricao

    def excluir_tarefa(self, indice: int):
        self.indice = indice
        for indice in tarefas:
            -indice

    def listar_tarefas(self):
        print(tarefas)
        return tarefas