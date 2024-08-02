# ui.py

from tkinter import *
from tkinter import ttk
from actions import Actions
from database import montar_tabelas

class App(Actions):
    """Classe que cria a aplicação para cadastro de clientes"""

    def __init__(self):
        """Inicializa a aplicação, configura a janela e seus componentes"""
        self.janela = Tk()  # Instancia o objeto janela
        self.tela()
        self.frames()
        self.todos_objetos()
        self.exibir_clientes()
        montar_tabelas()
        self.select_lista()
        self.menu_app()
        self.janela.mainloop()

    def tela(self):
        """Configura as propriedades básicas da janela"""
        self.janela.title("Cadastro de Clientes")
        self.janela.configure(background="black")
        self.janela.geometry("600x400")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=800, height=600)
        self.janela.minsize(width=500, height=300)

    def frames(self):
        """Cria e posiciona os frames na janela principal"""
        self.frame1 = Frame(self.janela, bd=4, bg="#36454F")
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame2 = Frame(self.janela, bd=4, bg="#36454F")
        self.frame2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.47)

    def todos_objetos(self):
        """Adiciona todos os widgets (botões, labels, entradas) ao frame1"""
        txt_fonte = "verdana"

        self.but_limpar = Button(self.frame1, text="Limpar Campos",
                                 border=4, bg="#2F4F4F", fg="white",
                                 font=(txt_fonte, 8, "bold"),
                                 command=self.limpar_dados)
        self.but_limpar.place(relx=0.02, rely=0.8, relwidth=0.20, relheight=0.15)

        self.but_buscar = Button(self.frame1, text="Buscar Código",
                                 border=4, bg="#2F4F4F", fg="white",
                                 font=(txt_fonte, 8, "bold"),
                                 command=self.buscar_cliente)
        self.but_buscar.place(relx=0.225, rely=0.8, relwidth=0.18, relheight=0.15)

        self.but_novo = Button(self.frame1, text="Novo Cliente",
                               border=4, bg="green", fg="white",
                               font=(txt_fonte, 8, "bold"), command=self.add_cliente)
        self.but_novo.place(relx=0.405, rely=0.8, relwidth=0.18, relheight=0.15)

        self.but_alterar = Button(self.frame1, text="Alterar Cliente",
                                  border=4, bg="#2F4F4F", fg="white",
                                  font=(txt_fonte, 8, "bold"), command=self.atualizar_cliente)
        self.but_alterar.place(relx=0.59, rely=0.8, relwidth=0.18, relheight=0.15)

        self.but_apagar = Button(self.frame1, text="Apagar Cliente",
                                 border=4, bg="red", fg="white",
                                 font=(txt_fonte, 8, "bold"), command=self.del_cliente)
        self.but_apagar.place(relx=0.775, rely=0.8, relwidth=0.20, relheight=0.15)

        self.lb_cod = Label(self.frame1, text="Código", bg="#36454F", fg="white",
                            font=(txt_fonte, 10, "bold"))
        self.lb_cod.place(relx=0.01, rely=0.05)
        self.entrada_cod = Entry(self.frame1)
        self.entrada_cod.place(relx=0.01, rely=0.17, relwidth=0.1)

        self.lb_nome = Label(self.frame1, text="Nome", bg="#36454F", fg="white",
                             font=(txt_fonte, 10, "bold"))
        self.lb_nome.place(relx=0.13, rely=0.05)
        self.entrada_nome = Entry(self.frame1)
        self.entrada_nome.place(relx=0.13, rely=0.17, relwidth=0.5)

        self.lb_tel = Label(self.frame1, text="Telefone", bg="#36454F", fg="white",
                            font=(txt_fonte, 10, "bold"))
        self.lb_tel.place(relx=0.01, rely=0.39)
        self.entrada_tel = Entry(self.frame1)
        self.entrada_tel.place(relx=0.01, rely=0.52, relwidth=0.3)

        self.lb_cidade = Label(self.frame1, text="Cidade", bg="#36454F", fg="white",
                               font=(txt_fonte, 10, "bold"))
        self.lb_cidade.place(relx=0.31, rely=0.39)
        self.entrada_cidade = Entry(self.frame1)
        self.entrada_cidade.place(relx=0.31, rely=0.52, relwidth=0.4)

    def exibir_clientes(self):
        """Configura a lista para exibir os clientes no frame2"""
        self.lista_cli = ttk.Treeview(self.frame2, height=3, column=("col1", "col2", "col3", "col4"))
        self.lista_cli.heading("#0", text="")
        self.lista_cli.heading("#1", text="Código")
        self.lista_cli.heading("#2", text="Nome")
        self.lista_cli.heading("#3", text="Telefone")
        self.lista_cli.heading("#4", text="Cidade")

        self.lista_cli.column("#0", width=1)
        self.lista_cli.column("#1", width=50)
        self.lista_cli.column("#2", width=200)
        self.lista_cli.column("#3", width=125)
        self.lista_cli.column("#4", width=125)

        self.lista_cli.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)

        self.scrollLista = Scrollbar(self.frame2, orient="vertical")
        self.lista_cli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.05, relwidth=0.04, relheight=0.9)
        self.lista_cli.bind("<Double-1>", self.duplo_clique)

    def menu_app(self):
        """Cria um menu na janela principal com opções adicionais"""
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opções", menu=file_menu)
        file_menu.add_command(label="Sair", command=self.janela.quit)
