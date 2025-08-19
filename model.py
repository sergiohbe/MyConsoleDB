from persistencia import Mongo

class Model():

    def __init__(self, controller):
        self.controller = controller
        self.persistencia = Mongo()
        self.own, self.had, self.wish = self.persistencia.carregar_listas()

    def save_lists(self):
        self.persistencia.salvar_listas(self.own, self.had, self.wish)

    #Função para chamar o catálogo
    def get_catalog(self):
        return self.persistencia.get_catalogo()

    #Adiciona a lista "Tenho"
    def add_own(self, console):
        if console not in self.own:
            self.own.append(console)
            self.save_lists()

    #Adiciona a lista "Já Tive"
    def add_had(self, console):
        if console not in self.had:
            self.had.append(console)
            self.save_lists()

    #Adiciona a lista "Wishlist"
    def add_wish(self, console):
        if console not in self.wish:
            self.wish.append(console)
            self.save_lists()

    def remover_own(self, console):
        if console in self.own:
            self.own.remove(console)
            self.save_lists()

    def remover_had(self, console):
        if console in self.had:
            self.had.remove(console)
            self.save_lists()

    def remover_wish(self, console):
        if console in self.wish:
            self.wish.remove(console)
            self.save_lists()

    def remove_all(self):
        self.own.clear()
        self.had.clear()
        self.wish.clear()
        self.save_lists()