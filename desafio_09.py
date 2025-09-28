#importando pacote

import mysql.connector


"""
fsymbols
"""

print("""
░█▀▀█ █──█ ▀▀█▀▀ █──█ █▀▀█ █▀▀▄ ░█▀▀▀█ █▀▀ █──█ █▀▀█ █▀▀█ █── █▀▀ 
░█▄▄█ █▄▄█ ──█── █▀▀█ █──█ █──█ ─▀▀▀▄▄ █── █▀▀█ █──█ █──█ █── ▀▀█ 
░█─── ▄▄▄█ ──▀── ▀──▀ ▀▀▀▀ ▀──▀ ░█▄▄▄█ ▀▀▀ ▀──▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀""")

print("Cadastre a Categoria")
nome = input("Nome: ")




# --- 1. CONFIGURAÇÃO DA CONEXÃO ---
# Substitua os valores entre aspas pelos seus dados
db_config = {
    "host": "localhost",  # Ou o IP do seu servidor MySQL
    "user": "root",
    "password": "",
    "database": "lms"
}

# --- 2. DADOS A SEREM INSERIDOS ---
nome_nova_categoria = nome

# O ID será gerado automaticamente pelo MySQL se for AUTO_INCREMENT

# --- 3. ESTABELECENDO E USANDO A CONEXÃO ---
try:
    # Conecta ao banco de dados
    """
     Os dois asteriscos(**) servem para desempacotar(unpack) um dicionário e passar seus pares de chave - valor como argumentos nomeados(keywords arguments) para
    uma
    função.
    """

    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()

    # Consulta SQL para inserção. Usamos %s como placeholder (seguro!)
    sql_insert = "INSERT INTO categoria (nome) VALUES (%s)"

    # Os dados a serem inseridos, sempre como uma tupla
    dados_categoria = (nome_nova_categoria,)

    # Executa a consulta
    cursor.execute(sql_insert, dados_categoria)

    # Confirma a transação (MUITO IMPORTANTE!)
    conexao.commit()

    print(f"Sucesso! Categoria '{nome_nova_categoria}' inserida com o ID: {cursor.lastrowid}")

except mysql.connector.Error as erro:
    print(f"Erro ao inserir a categoria: {erro}")
    # Se houve um erro, desfazemos quaisquer alterações
    if 'conexao' in locals() and conexao.is_connected():
        conexao.rollback()

finally:
    # --- 4. FECHANDO CONEXÕES ---
    # Garante que o cursor e a conexão sejam fechados, mesmo se houver erro
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão com o MySQL fechada.")