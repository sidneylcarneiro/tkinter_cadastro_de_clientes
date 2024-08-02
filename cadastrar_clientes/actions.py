# actions.py

from database import conectar_bd, desconectar_bd
from tkinter import END

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

    def add_cliente(self):
        """Adiciona um novo cliente à tabela de clientes"""
        self.variaveis_bd()
        con, cursor = conectar_bd()
        cursor.execute("""INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
        con.commit()
        desconectar_bd(con)
        self.select_lista()
        self.limpar_dados()

    def select_lista(self):
        """Seleciona e exibe todos os clientes na interface"""
        self.lista_cli.delete(*self.lista_cli.get_children())
        con, cursor = conectar_bd()
        lista = cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.lista_cli.insert("", END, values=i)

        desconectar_bd(con)

    def buscar_cliente(self):
        """Busca um cliente pelo código, preenche os campos de entrada e destaca na lista"""
        self.variaveis_bd()
        con, cursor = conectar_bd()
        cliente = cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE cod = ?""", (self.codigo,)).fetchone()

        if cliente:
            self.limpar_dados()
            self.entrada_cod.insert(END, cliente[0])
            self.entrada_nome.insert(END, cliente[1])
            self.entrada_tel.insert(END, cliente[2])
            self.entrada_cidade.insert(END, cliente[3])

            for item in self.lista_cli.get_children():
                if self.lista_cli.item(item, 'values')[0] == cliente[0]:
                    self.lista_cli.selection_set(item)
                    self.lista_cli.see(item)
                    break

        desconectar_bd(con)

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
        self.variaveis_bd()
        con, cursor = conectar_bd()
        cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.codigo,))
        con.commit()
        desconectar_bd(con)
        self.limpar_dados()
        self.select_lista()

    def atualizar_cliente(self):
        self.variaveis_bd()
        con, cursor = conectar_bd()
        cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
        con.commit()
        desconectar_bd(con)
        self.select_lista()
        self.limpar_dados()
