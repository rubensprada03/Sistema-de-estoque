import sqlite3 as lite 

#criando conexao    
con = lite.connect('dados.db')

#criando tabela
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventorio(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, Local TEXT,descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
    
