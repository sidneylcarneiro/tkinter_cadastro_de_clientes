from tkinter import *
from tkinter import ttk
import sqlite3 as sql

# Define a fonte padrão utilizada na interface
txt_fonte = "verdana"

# Cria o objeto principal da janela
janela = Tk()

class Actions:
    """Classe das ações de Backend"""

    def variaveis_bd(self):
        # Captura os dados dos campos de entrada
        self.codigo = self.entrada_cod.get()
        self.nome = self.entrada_nome.get()
        self.telefone = self.entrada_tel.get()
        self.cidade = self.entrada_cidade.get()

    def limpar_dados(self):
        """Limpa os campos de entrada de texto"""
        self.entrada_cidade.delete(0, END)
        self.entrada_tel.delete(0, END)
        self.entrada_nome.delete(0, END)
        self.entrada_cod.delete(0, END)

    def conectar_bd(self):
        """Conecta ao banco de dados SQLite"""
        self.con = sql.connect("clientes.bd")
        self.cursor = self.con.cursor()
        print("Conectando ao banco de dados...")

    def desconectar_bd(self):
        """Fecha a conexão com o banco de dados"""
        self.con.close()
        print("Desconectando do banco de dados...")

    def montar_tabelas(self):
        """Cria a tabela de clientes no banco de dados, se não existir"""
        self.conectar_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_cliente CHAR(40) NOT NULL,
                telefone CHAR(20),
                cidade CHAR(40) 
            )
            """)
        self.con.commit()
        print("Banco de dados criado.")
        self.desconectar_bd()

    def add_cliente(self):
        """Adiciona um novo cliente à tabela de clientes"""
        # Captura os dados dos campos de entrada
        self.variaveis_bd()

        # Conecta ao banco de dados e insere os dados do cliente
        self.conectar_bd()
        self.cursor.execute("""INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
        self.con.commit()
        self.desconectar_bd()

        # Atualiza a lista de clientes exibida na interface
        self.select_lista()
        self.limpar_dados()

    def select_lista(self):
        """Seleciona e exibe todos os clientes na interface"""
        # Limpa a lista de clientes exibida
        self.lista_cli.delete(*self.lista_cli.get_children())

        # Conecta ao banco de dados e recupera os dados dos clientes
        self.conectar_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)

        # Insere os dados na interface
        for i in lista:
            self.lista_cli.insert("", END, values=i)

        self.desconectar_bd()

    def buscar_cliente(self):
        """Busca um cliente pelo código, preenche os campos de entrada e destaca na lista"""

        # Captura o código do campo de entrada
        self.variaveis_bd()

        # Conecta ao banco de dados e busca pelo código
        self.conectar_bd()
        cliente = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE cod = ?""", (self.codigo,)).fetchone()

        # Se um cliente for encontrado, preenche os campos de entrada e seleciona na lista
        if cliente:
            # Limpa os campos de entrada
            self.limpar_dados()

            # Preenche os campos de entrada com os dados do cliente encontrado
            self.entrada_cod.insert(END, cliente[0])
            self.entrada_nome.insert(END, cliente[1])
            self.entrada_tel.insert(END, cliente[2])
            self.entrada_cidade.insert(END, cliente[3])

            # Percorre a lista de clientes e destaca o cliente encontrado
            for item in self.lista_cli.get_children():
                if self.lista_cli.item(item, 'values')[0] == cliente[0]:
                    self.lista_cli.selection_set(item)
                    self.lista_cli.see(item)  # Garante que o item esteja visível na lista
                    break

        self.desconectar_bd()

    def duplo_clique(self, event):
        self.limpar_dados()
        self.lista_cli.selection()
        for a in self.lista_cli.selection():
            col1, col2, col3, col4 = self.lista_cli.item(a, "values")
            self.entrada_cod.insert(END, col1)
            self.entrada_nome.insert(END, col2)
            self.entrada_tel.insert(END, col3)
            self.entrada_cidade.insert(END, col4)

    def del_cliente(self):
        # Captura os dados dos campos de entrada
        self.variaveis_bd()
        self.conectar_bd()

        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo,))
        self.con.commit()
        self.desconectar_bd()
        self.limpar_dados()
        self.select_lista()

    def atualizar_cliente(self):
        self.variaveis_bd()
        self.conectar_bd()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
        self.con.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpar_dados()

class App(Actions):
    """Classe que cria a aplicação para cadastro de clientes"""

    def __init__(self):
        """Inicializa a aplicação, configura a janela e seus componentes"""
        # Inicializa a janela principal e seus componentes
        self.janela = janela  # Instancia o objeto janela dentro da função
        self.tela()  # Configura a janela principal
        self.frames()  # Adiciona frames à janela
        self.todos_objetos()  # Adiciona todos os widgets necessários
        self.exibir_clientes()  # Configura a visualização dos clientes
        self.montar_tabelas()  # Se conecta ao banco de dados
        self.select_lista()  # Atualiza lista de clientes
        self.menu_app()
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
        self.but_limpar = Button(self.frame1, text="Limpar Campos",
                                 border=4, bg="#2F4F4F", fg="white",
                                 font=(txt_fonte, 8, "bold"),
                                 command=self.limpar_dados)
        self.but_limpar.place(relx=0.02, rely=0.8, relwidth=0.20, relheight=0.15)

        # Botão para buscar um cliente
        self.but_buscar = Button(self.frame1, text="Buscar Código",
                                 border=4, bg="#2F4F4F", fg="white",
                                 font=(txt_fonte, 8, "bold"),
                                 command=self.buscar_cliente)  # Chama o método buscar_cliente
        self.but_buscar.place(relx=0.225, rely=0.8, relwidth=0.18, relheight=0.15)

        # Botão para adicionar um novo cliente
        self.but_novo = Button(self.frame1, text="Novo Cliente",
                               border=4, bg="green", fg="white",
                               font=(txt_fonte, 8, "bold"), command=self.add_cliente)
        self.but_novo.place(relx=0.405, rely=0.8, relwidth=0.18, relheight=0.15)

        # Botão para atualizar um cliente existente
        self.but_alterar = Button(self.frame1, text="Alterar Cliente",
                                  border=4, bg="#2F4F4F", fg="white",
                                  font=(txt_fonte, 8, "bold"), command=self.atualizar_cliente)
        self.but_alterar.place(relx=0.59, rely=0.8, relwidth=0.19, relheight=0.15)

        # Botão para apagar um cliente
        self.but_apagar = Button(self.frame1, text="Excluir Cliente",
                                 border=4, bg="#722F37", fg="white",
                                 font=(txt_fonte, 8, "bold"), command=self.del_cliente)
        self.but_apagar.place(relx=0.785, rely=0.8, relwidth=0.20, relheight=0.15)

        # Rótulo (label) para o Nome do Programa
        self.rotulo_prog = Label(self.frame1, text="Cadastro de Clientes",
                                 fg="white", bg="black", font=("arial", 16, "bold"))
        self.rotulo_prog.place(relx=0.42, rely=0.04, relwidth=0.57, relheight=0.15)

        # Rótulo (label) para o campo Código do cliente
        self.rotulo_cod = Label(self.frame1, text="Código",
                                fg="white", bg="black", font=(txt_fonte, 8))
        self.rotulo_cod.place(relx=0.02, rely=0.04, relwidth=0.1, relheight=0.15)

        # Entrada de texto para o Código do cliente
        self.entrada_cod = Entry(self.frame1, font=(txt_fonte, 8))
        self.entrada_cod.place(relx=0.15, rely=0.04, relwidth=0.25, relheight=0.15)

        # Rótulo (label) para o campo Nome do cliente
        self.rotulo_nome = Label(self.frame1, text="Nome",
                                 fg="white", bg="black", font=(txt_fonte, 8))
        self.rotulo_nome.place(relx=0.02, rely=0.3, relwidth=0.1, relheight=0.15)

        # Entrada de texto para o Nome do cliente
        self.entrada_nome = Entry(self.frame1, font=(txt_fonte, 8))
        self.entrada_nome.place(relx=0.149, rely=0.3, relwidth=0.837, relheight=0.15)

        # Rótulo (label) para o campo Telefone do cliente
        self.rotulo_tel = Label(self.frame1, text="Telefone",
                                fg="white", bg="black", font=(txt_fonte, 8))
        self.rotulo_tel.place(relx=0.02, rely=0.55, relwidth=0.1, relheight=0.15)

        # Entrada de texto para o Telefone do cliente
        self.entrada_tel = Entry(self.frame1, font=(txt_fonte, 8))
        self.entrada_tel.place(relx=0.149, rely=0.55, relwidth=0.3, relheight=0.15)

        # Rótulo (label) para o campo Cidade do cliente
        self.rotulo_cidade = Label(self.frame1, text="Cidade",
                                   fg="white", bg="black", font=(txt_fonte, 8))
        self.rotulo_cidade.place(relx=0.475, rely=0.55, relwidth=0.1, relheight=0.15)

        # Entrada de texto para a Cidade do cliente
        self.entrada_cidade = Entry(self.frame1, font=(txt_fonte, 8))
        self.entrada_cidade.place(relx=0.6, rely=0.55, relwidth=0.385, relheight=0.15)

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

        self.lista_cli.bind("<Double-1>", self.duplo_clique)

    def menu_app(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def exit_app(): self.janela.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Sobre", menu=filemenu2)
        filemenu.add_command(label="Sair", command=exit_app)
        filemenu2.add_command(label="Limpa Cliente", command=self.limpar_dados)

# Instancia e executa a aplicação
App()
