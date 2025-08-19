import tkinter
from tkinter import ttk

class View():

    def __init__(self, controller):
        self.controller = controller
        self.root = tkinter.Tk()
        self.tela_inicial()

    #Função para limpar a tela
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()    
    
    def adicionar_own(self):
        console = self.combo.get()
        if console != "Console":
            self.controller.add_own(console)

    def adicionar_had(self):
        console = self.combo.get()
        if console != "Console":
            self.controller.add_had(console)

    def adicionar_wish(self):
        console = self.combo.get()
        if console != "Console":
            self.controller.add_wish(console)

    def remover_tem(self, console):
        self.controller.remove_own(console)
        self.tela_tem() #recarrega a tela depois de remover

    def remover_teve(self, console):
        self.controller.remove_had(console)
        self.tela_teve()

    def remover_desejo(self, console):
        self.controller.remove_wish(console)
        self.tela_wishlist()

    def tela_inicial(self):
        self.clear_screen()
        self.root.title("MyConsoleDb - Tela inicial") #titulo da pagina
        self.root.geometry("1200x1200") #tamanho da tela

        TitleText = tkinter.Label(self.root, text="MyConsoleDb", font=("Arial", 24, 'bold')) #titulo da tela "literal", vai ser o texto que vai aparecer acima da ChoiceBox
        TitleText.place(relx=0.5, rely=0.05, anchor="n")

        #Pega o repasse do catalogo do controller
        ConsoleCatalog = self.controller.get_catalog()

        #Caixa de escolha
        self.combo = ttk.Combobox(self.root, values=ConsoleCatalog, state="readonly")
        self.combo.place(relx=0.5, rely=0.175, anchor="center", width=200, height=25)
        self.combo.set("Console")

        #Botoes
        OwnButton = tkinter.Button(self.root, text="Tenho", width=10, height=2,
        command=self.adicionar_own)
        OwnButton.place(relx=0.65, rely=0.15, anchor="ne")

        HadButton = tkinter.Button(self.root, text="Tive", width=10, height=2,
        command=self.adicionar_had)
        HadButton.place(relx=0.65, rely=0.25, anchor="ne")

        WishlistButton = tkinter.Button(self.root, text="Wishlist", width=10,
        height=2, command=self.adicionar_wish)
        WishlistButton.place(relx=0.65, rely=0.35, anchor="ne")

        GoToCollectionButton = tkinter.Button(self.root, text="Coleção", width=15, height=2, 
        command=self.tela_colecao)
        GoToCollectionButton.place(relx=0.98, rely=0.98, anchor="se")

        ExitButton = tkinter.Button(self.root, text="Sair", width=15, height=2, command=self.controller.sair)
        ExitButton.place(relx=0.02, rely=0.98, anchor="sw")

    def tela_colecao(self):
        self.clear_screen()
        self.root.title("MyConsoleDb - Coleção")
        self.root.geometry("1200x1200")

        TitleText = tkinter.Label(self.root, text="Coleção", font=("Arial", 18, 'bold'))
        TitleText.place(relx=0.5, rely=0.02, anchor="n")

        GoToOwnedConsolesButton = tkinter.Button(self.root, text="Coleção Atual", width=15, height=4,
        command=self.tela_tem)
        GoToOwnedConsolesButton.place(relx=0.5, rely=0.15, anchor="center")

        GoToConsolesHadButton = tkinter.Button(self.root, text="Consoles que já teve", width=15, height=4, 
        command=self.tela_teve)
        GoToConsolesHadButton.place(relx=0.5, rely=0.25, anchor="center")
        
        GoToWishlistButton = tkinter.Button(self.root, text="Wishlist", width=15, height=4, 
        command=self.tela_wishlist)
        GoToWishlistButton.place(relx=0.5, rely=0.35, anchor="center")              

        GoToInitialScreenButton = tkinter.Button(self.root, text="Tela Inicial", width=15, height=2, 
        command=self.tela_inicial)
        GoToInitialScreenButton.place(relx=0.02, rely=0.02, anchor="nw")
        
        ResetCollectionButton = tkinter.Button(self.root, text="Limpar Listas", width=15, height=2,
        command=self.controller.remover_todos)
        ResetCollectionButton.place(relx=0.5, rely=0.5, anchor="s")

        ExitButton = tkinter.Button(self.root, text="Sair", width=15, height=2, command=self.controller.sair)
        ExitButton.place(relx=0.02, rely=0.98, anchor="sw")                
    
    def tela_tem(self):
        self.clear_screen()
        self.root.title("MyConsoleDb - Consoles que tem")
        self.root.geometry("1200x1200")

        TitleText = tkinter.Label(self.root, text="Consoles que tem", font=("Arial", 18, 'bold'))
        TitleText.place(relx=0.5, rely=0.02, anchor="n")

        #Lista
        lista1 = self.controller.get_own_list()

        for i, console in enumerate(lista1):
            label = tkinter.Label(self.root, text=console, font=("Arial", 14))
            label.place(x=600, y=100 + i * 40)

            botao_remover1 = tkinter.Button(self.root, text="Remover",
            command=lambda c=console: self.remover_tem(c))
            botao_remover1.place(x=800, y=100 + i * 40)


        GoToInitialScreenButton = tkinter.Button(self.root, text="Tela Inicial", width=15, height=2, 
        command=self.tela_inicial)
        GoToInitialScreenButton.place(relx=0.02, rely=0.02, anchor="nw")        

        GoToCollectionButton = tkinter.Button(self.root, text="Coleção", width=15, height=2, 
        command=self.tela_colecao)
        GoToCollectionButton.place(relx=0.02, rely=0.12, anchor="nw")        

        ExitButton = tkinter.Button(self.root, text="Sair", width=15, height=2, command=self.controller.sair)
        ExitButton.place(relx=0.02, rely=0.98, anchor="sw")        
    
    def tela_teve(self):
        self.clear_screen()
        self.root.title("MyConsoleDb - Consoles que já teve")
        self.root.geometry("1200x1200")

        TitleText = tkinter.Label(self.root, text="Consoles que já teve", font=("Arial", 18, 'bold'))
        TitleText.place(relx=0.5, rely=0.02, anchor="n")

        lista2 = self.controller.get_had_list()

        for i, console in enumerate(lista2):
            label = tkinter.Label(self.root, text=console, font=("Arial", 14))
            label.place(x=600, y=100 + i * 40)

            botao_remover2 = tkinter.Button(self.root, text="Remover",
            command=lambda c=console: self.remover_teve(c))
            botao_remover2.place(x=800, y=100 + i * 40)

        GoToInitialScreenButton = tkinter.Button(self.root, text="Tela Inicial", width=15, height=2, 
        command=self.tela_inicial)
        GoToInitialScreenButton.place(relx=0.02, rely=0.02, anchor="nw")        

        GoToCollectionButton = tkinter.Button(self.root, text="Coleção", width=15, height=2, 
        command=self.tela_colecao)
        GoToCollectionButton.place(relx=0.02, rely=0.12, anchor="nw")

        ExitButton = tkinter.Button(self.root, text="Sair", width=15, height=2, command=self.controller.sair)
        ExitButton.place(relx=0.02, rely=0.98, anchor="sw")
    
    def tela_wishlist(self):
        self.clear_screen()
        self.root.title("MyConsoleDb - Wishlist")
        self.root.geometry("1200x1200")

        TitleText = tkinter.Label(self.root, text="Wishlist", font=("Arial", 18, 'bold'))
        TitleText.place(relx=0.5, rely=0.02, anchor="n")

        lista3 = self.controller.get_wish_list()

        for i, console in enumerate(lista3):
            label = tkinter.Label(self.root, text=console, font=("Arial", 14))
            label.place(x=600, y=100 + i * 40)

            botao_remover3 = tkinter.Button(self.root, text="Remover",
            command=lambda c=console: self.remover_desejo(c))
            botao_remover3.place(x=800, y=100 + i * 40)

        GoToInitialScreenButton = tkinter.Button(self.root, text="Tela Inicial", width=15, height=2, 
        command=self.tela_inicial)
        GoToInitialScreenButton.place(relx=0.02, rely=0.02, anchor="nw")        

        GoToCollectionButton = tkinter.Button(self.root, text="Coleção", width=15, height=2, 
        command=self.tela_colecao)
        GoToCollectionButton.place(relx=0.02, rely=0.12, anchor="nw")

        ExitButton = tkinter.Button(self.root, text="Sair", width=15, height=2, command=self.controller.sair)
        ExitButton.place(relx=0.02, rely=0.98, anchor="sw")

    def start(self):
        self.root.mainloop()