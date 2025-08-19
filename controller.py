import tkinter

from model import Model
from view import View

class Controller():
    
    def __init__(self, view, model):
        self.model = model
        self.view = view

    def get_own_list(self):
        return self.model.own

    def get_had_list(self):
        return self.model.had

    def get_wish_list(self):
        return self.model.wish        

    #Adiciona a lista "Tenho"
    def add_own(self, console):
        self.model.add_own(console)

    #Adiciona a lista "Já Tive"
    def add_had(self, console):
        self.model.add_had(console)

    #Adiciona a lista "Wishlist"
    def add_wish(self, console):
        self.model.add_wish(console)

    def remove_own(self, console):
        self.model.remover_own(console)

    def remove_had(self, console):
        self.model.remover_had(console)

    def remove_wish(self, console):
        self.model.remover_wish(console)

    def remover_todos(self):
        self.model.remove_all()    

    #Repassa o comando para a View encerrar a aplicação
    def sair(self):
        self.view.root.destroy()

    #Pega o catálogo do model
    def get_catalog(self):
        return self.model.get_catalog()