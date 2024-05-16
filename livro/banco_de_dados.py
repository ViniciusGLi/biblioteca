import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="dados"
)
cursor= con.cursor()


cursor.execute('CREATE  TABLE livros(\
               id INTEGER AUTO_INCREMENT PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                editora TEXT,\
                ano_publicacao INTEGER,\
                isbn TEXT)') 

cursor.execute('CREATE  TABLE usuarios(\
               id INTEGER AUTO_INCREMENT PRIMARY KEY,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco TEXT,\
                email TEXT,\
                telefone TEXT)') 

cursor.execute('CREATE  TABLE emprestimos(\
               id INTEGER AUTO_INCREMENT PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREIGN KEY(id_livro) REFERENCES livros(id),\
                FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')




cursor.close