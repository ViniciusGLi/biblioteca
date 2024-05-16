import mysql.connector

def connect(): 
 conn= mysql.connector.connect(
    host     = "localhost",
    user     = "root",
    password = "1234",
    database = "dados")
 return conn

def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    cursor = conn.cursor()  # Cria um objeto cursor
    cursor.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES (%s, %s, %s, %s, %s)",
                   (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()  # Não se esqueça de fazer commit das alterações
    conn.close()
  
    
def insert_user(nome,sobrenome, endereco, email, telefone):
    conn= connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES (%s, %s, %s, %s, %s)",
                 (nome, sobrenome, endereco, email, telefone))
    conn.commit()  # Não se esqueça de fazer commit das alterações
    conn.close()
    

def exibir_livros():
    conn = connect()
    cursor = conn.cursor()
    livros = cursor.execute("SELECT *  FROM livros")
    rows = cursor.fetchall()
    
    if not rows:
        print("Nenhum livro encontrado na biblitoeca")
        return
    
    print("Livros na bblioteca: ")
    for livros in rows:
        print(f"ID: {livros[0]}")
        print(f"Titulo: {livros[1]}")
        print(f"Autor: {livros[2]}")
        print(f"Editora: {livros[3]}")
        print(f"Ano de Publicacao: {livros[4]}")
        print(f"Isbn: {livros[5]}")
        print("\n")

def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES(%s, %s, %s, %s) ", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()
    
def get_books_on_loan():
    conn = connect()
    cursor = conn.cursor()  # Cria um objeto cursor
    cursor.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                    FROM livros \
                    INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                    INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                    WHERE emprestimos.data_devolucao IS NULL")
    result = cursor.fetchall()  # Busca todas as linhas
    conn.commit()
    cursor.close()
    conn.close()
    return result

def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    cursor = conn.cursor()  # Cria um objeto cursor
    cursor.execute("UPDATE emprestimos SET data_devolucao = %s WHERE id = %s", (data_devolucao, id_emprestimo))
    conn.commit()  # Não se esqueça de fazer commit das alterações
    cursor.close()
    conn.close()

# insert_book("One Piece", "Oda", "Nao sei", 5662, "5788598270692")

'''# Exemplo de uso das funções
insert_book("One Piece", "Oda", "Nao sei", 5662, "5788598270692")
insert_user("João", "Silva", "Rua A, 123", "joao.silva@email.com", "(11) 1234-5678")
insert_loan(1, 1, "2022-03-25", None)
books_on_loan = get_books_on_loan()
print(books_on_loan)
update_loan_return_date(1, "2022-03-28")'''
