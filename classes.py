
class ToDoList:

    def __init__ (self, descricao, indice):
        self.__descricao = descricao
        self.indice = indice

    def adicionar_tarefa(self, descricao: str):
        self.__descricao = descricao
        return descricao

    def excluir_tarefa(self, indice: int):
        self.__indice = indice
    
    def get_Descricao(self, descricao):
        return descricao
    
    def set_Descricao(self, nova_descricao):
        self.__descricao = nova_descricao
        return nova_descricao
    
    def get_Descricao(self, indice):
        return indice
    
    def set_Descricao(self, novo_indice):
        self.__indice = novo_indice
        return novo_indice
    