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
    
def get_user():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    users = cursor.fetchall()
    conn.close()
    return users

    return livros

def exibir_livros():
    conn = connect()
    cursor = conn.cursor()
    livros = cursor.execute("SELECT *  FROM livros")
    rows = cursor.fetchall()
    return rows
  

def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES(%s, %s, %s, %s) ", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()
    
def get_books_on_loan():
    conn = connect()
    cursor = conn.cursor()  # Cria um objeto cursor
    cursor.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM livros \
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.data_devolucao IS NULL")
    result = cursor.fetchall()  # Busca todas as linhas
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

#insert_book("One Piece", "Oda", "Nao sei", 5662, "5788598270692")
#insert_user("João", "Silva", "Rua A, 123", "joao.silva@email.com", "(11) 1234-5678")
insert_loan(1, 1, "2022-03-25", None)
#books_on_loan = get_books_on_loan()
#print(books_on_loan)
#update_loan_return_date(1, "2022-03-28")'''
