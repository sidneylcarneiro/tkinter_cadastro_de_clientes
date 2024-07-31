from tkinter import *
from tkinter import ttk

# Define a fonte padrão utilizada na interface
txt_fonte = "verdana"

# Cria o objeto principal da janela
janela = Tk()


class App:
    """Classe que cria a aplicação para cadastro de clientes"""

    def __init__(self):
        """Inicializa a aplicação, configura a janela e seus componentes"""

        self.janela = janela  # instancia o objeto janela dentro da função
        self.tela()  # Configura a janela principal
        self.frames()  # Adiciona frames à janela
        self.todos_objetos()  # Adiciona todos os widgets necessários
        self.exibir_clientes()  # Configura a visualização dos clientes

        # Inicia o loop principal da aplicação, mantendo a janela aberta
        janela.mainloop()

    def tela(self):
        """Configura as propriedades básicas da janela"""
        self.janela.title("Cadastro de Clientes")  # Define o título da janela
        self.janela.configure(background="black")  # Define a cor de fundo da janela
        self.janela.geometry("600x400")  # Define o tamanho inicial da janela
        self.janela.resizable(True, True)  # Permite que a janela seja redimensionada
        self.janela.maxsize(width=800, height=600)  # Define o tamanho máximo da janela
        self.janela.minsize(width=500, height=300)  # Define o tamanho mínimo da janela

    def frames(self):
        """Cria e posiciona os frames na janela principal"""

        # Cria o primeiro frame para os controles principais
        self.frame1 = Frame(self.janela, bd=4, bg="#36454F")

        # Posiciona o frame1 na janela com coordenadas relativas
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        # Cria o segundo frame para a exibição de dados dos clientes
        self.frame2 = Frame(self.janela, bd=4, bg="#36454F")

        # Posiciona o frame2 logo abaixo do frame1
        self.frame2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.47)

    def todos_objetos(self):
        """Adiciona todos os widgets (botões, labels, entradas) ao frame1"""

        # Botão para limpar os dados inseridos
        self.but_limpar = Button(self.frame1, text="limpar",
                                 border=4, bg="#2F4F4F", fg="white",
                                 font=(txt_fonte, 8, "bold"))
        self.but_limpar.place(relx=0.05, rely=0.2, relwidth=0.1, relheight=0.15)

        # Botão para buscar um cliente
        self.but_buscar = Button(self.frame1, text="buscar",
                                 border=4, bg="#2F4F4F", fg="white",
                                 font=(txt_fonte, 8, "bold"))
        self.but_buscar.place(relx=0.165, rely=0.2, relwidth=0.1, relheight=0.15)

        # Botão para adicionar um novo cliente
        self.but_novo = Button(self.frame1, text="novo",
                               border=4, bg="#2F4F4F", fg="white",
                               font=(txt_fonte, 8, "bold"))
        self.but_novo.place(relx=0.42, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão para alterar os dados de um cliente existente
        self.but_alterar = Button(self.frame1, text="alterar",
                                  border=4, bg="#2F4F4F", fg="white",
                                  font=(txt_fonte, 8, "bold"))
        self.but_alterar.place(relx=0.53, rely=0.1, relwidth=0.1, relheight=0.15)

        # Botão para apagar um cliente
        self.but_apagar = Button(self.frame1, text="apagar",
                                 border=4, bg="#2F4F4F", fg="white",
                                 font=(txt_fonte, 8, "bold"))
        self.but_apagar.place(relx=0.64, rely=0.1, relwidth=0.1, relheight=0.15)

        # Rótulo (label) para o campo Código do cliente
        self.rotulo_cod = Label(self.frame1, text="Código",
                                fg="white", bg="black", font=(txt_fonte, 8))
        self.rotulo_cod.place(relx=0.05, rely=0.03, relwidth=0.1, relheight=0.15)

        # Entrada de texto para o Código do cliente
        self.entrada_cod = Entry(self.frame1, font=(txt_fonte, 8))
        self.entrada_cod.place(relx=0.165, rely=0.03, relwidth=0.1, relheight=0.15)

        # Rótulo (label) para o campo Nome do cliente
        self.rotulo_nome = Label(self.frame1, text="Nome",
                                 fg="white", bg="black", font=(txt_fonte, 8))
        self.rotulo_nome.place(relx=0.05, rely=0.45, relwidth=0.1, relheight=0.15)

        # Entrada de texto para o Nome do cliente
        self.entrada_nome = Entry(self.frame1, font=(txt_fonte, 8))
        self.entrada_nome.place(relx=0.165, rely=0.45, relwidth=0.8, relheight=0.15)

        # Rótulo (label) para o campo Telefone do cliente
        self.rotulo_tel = Label(self.frame1, text="Telefone",
                                fg="white", bg="black", font=(txt_fonte, 8))
        self.rotulo_tel.place(relx=0.05, rely=0.65, relwidth=0.1, relheight=0.15)

        # Entrada de texto para o Telefone do cliente
        self.entrada_tel = Entry(self.frame1, font=(txt_fonte, 8))
        self.entrada_tel.place(relx=0.165, rely=0.65, relwidth=0.3, relheight=0.15)

        # Rótulo (label) para o campo Cidade do cliente
        self.rotulo_cidade = Label(self.frame1, text="Cidade",
                                   fg="white", bg="black", font=(txt_fonte, 8))
        self.rotulo_cidade.place(relx=0.49, rely=0.65, relwidth=0.1, relheight=0.15)

        # Entrada de texto para a Cidade do cliente
        self.entrada_cidade = Entry(self.frame1, font=(txt_fonte, 8))
        self.entrada_cidade.place(relx=0.61, rely=0.65, relwidth=0.355, relheight=0.15)

    def exibir_clientes(self):
        """Configura o frame2 para exibir a lista de clientes"""

        # Cria a tabela para mostrar os dados dos clientes
        self.lista_cli = ttk.Treeview(self.frame2, height=3, columns=("Col1", "Col2", "Col3", "Col4"))
        self.lista_cli.place(relx=0.01, rely=0.02, relwidth=0.97, relheight=0.95)

        # Adiciona uma barra de rolagem vertical à tabela
        self.barra_rolagem = Scrollbar(self.frame2, orient=VERTICAL, command=self.lista_cli.yview)
        self.barra_rolagem.place(relx=0.97, rely=0.02, relheight=0.95)

        # Conecta a barra de rolagem à lista de clientes
        self.lista_cli.configure(yscroll=self.barra_rolagem.set)

        # Define o cabeçalho das colunas da tabela
        self.lista_cli.heading("#0", text="")
        self.lista_cli.heading("#1", text="Código")
        self.lista_cli.heading("#2", text="Nome")
        self.lista_cli.heading("#3", text="Telefone")
        self.lista_cli.heading("#4", text="Cidade")

        # Define a largura das colunas da tabela
        self.lista_cli.column("#0", width=1)
        self.lista_cli.column("#1", width=50)
        self.lista_cli.column("#2", width=200)
        self.lista_cli.column("#3", width=125)
        self.lista_cli.column("#4", width=125)


# Instancia e executa a aplicação
App()
