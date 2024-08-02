# database.py

import sqlite3 as sql

def conectar_bd():
    """Conecta ao banco de dados SQLite"""
    con = sql.connect("clientes.bd")
    return con, con.cursor()

def desconectar_bd(con):
    """Fecha a conexão com o banco de dados"""
    con.close()

def montar_tabelas():
    """Cria a tabela de clientes no banco de dados, se não existir"""
    con, cursor = conectar_bd()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            cod INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cliente CHAR(40) NOT NULL,
            telefone CHAR(20),
            cidade CHAR(40) 
        )
        """)
    con.commit()
    desconectar_bd(con)
