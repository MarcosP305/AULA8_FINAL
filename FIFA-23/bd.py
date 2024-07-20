# importe
import sqlite3

# crie a conxão
conexao =  sqlite3.connect('meu_banco_de_dados.db')

# crie um cursor para poder executar a linguagem sql
cursor = conexao.cursor()

# Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
    ) 
''')

# iNSERIR DADOS NA TABELA
nome = 'Ana'
idade = 25
cidade = 'São Paulo'
cursor.execute('''
    INSERT INTO pessoas (nome, idade, cidade)
    VALUES (?, ?, ?)
''', (nome, idade, cidade))

# Confirma a transação
conexao.commit()

# Consultar dados da tabela
cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

# Mostra os dados consultados
for pessoa in pessoas:
    print(f'''ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade:{pessoa[2]}, Cidade: pessoa[3]''')

# Fechar a conexão
conexao.close()

