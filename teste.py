# import sqlite3

# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

# def delete_all_rows(transacoes):
#     query = f"DELETE FROM {transacoes};"
#     cursor.execute(query)
#     print(f"Deleted all rows from {transacoes}")


# delete_all_rows('transacoes')

# conn.commit()
# conn.close()

# import sqlite3

# # # Conectando ao banco de dados
# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

# # cursor.execute('''
# #     DROP TABLE adicoes;
# # ''')
# # cursor.execute('''
# #     DROP TABLE retiradas;
# # ''')

# # Função para clonar uma tabela
# def clone_table(alunos, adicoes):
#     # Passo 1: Criar a nova tabela com a mesma estrutura da tabela original
#     cursor.execute(f'''
#         CREATE TABLE {adicoes} AS SELECT * FROM {alunos} WHERE 0;
#     ''')

#     # Passo 2: Copiar os dados da tabela original para a nova tabela
#     cursor.execute(f'''
#         INSERT INTO {adicoes} SELECT * FROM {alunos};
#     ''')

#     print(f"Tabela '{alunos}' clonada para '{adicoes}'")

# # Exemplo: Clonar a tabela 'alunos' para 'alunos_clone'
# clone_table('alunos', 'adicoes')

# # Função para clonar uma tabela
# def clone_table(alunos, retiradas):
#     # Passo 1: Criar a nova tabela com a mesma estrutura da tabela original
#     cursor.execute(f'''
#         CREATE TABLE {retiradas} AS SELECT * FROM {alunos} WHERE 0;
#     ''')

#     # Passo 2: Copiar os dados da tabela original para a nova tabela
#     cursor.execute(f'''
#         INSERT INTO {retiradas} SELECT * FROM {alunos};
#     ''')

#     print(f"Tabela '{alunos}' clonada para '{retiradas}'")

# # Exemplo: Clonar a tabela 'alunos' para 'alunos_clone'
# clone_table('alunos', 'retiradas')

# # Comitando as mudanças e fechando a conexão
# conn.commit()
# conn.close()

# import sqlite3

# # Conectar ao banco de dados (altere 'database.db' para o caminho do seu banco de dados)
# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

# # Apagar o valor da célula (definindo como NULL)
# cursor.execute('UPDATE retiradas SET "Heryco Lemos Queirós" = 0 WHERE id = ?', (1,))

# # Confirmar as mudanças
# conn.commit()

# # Fechar a conexão
# conn.close()



import sqlite3

# Conectar ao banco de dados (altere 'database.db' para o caminho do seu banco de dados)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Apagar uma linha específica da tabela
cursor.execute('DELETE FROM retiradas WHERE id = ?', (244,))

# Confirmar as mudanças
conn.commit()

# Fechar a conexão
conn.close()
