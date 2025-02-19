import bcrypt
import mysql.connector
from mysql.connector import Error

def register(name, email, pw1, pw2):
    if pw1 == pw2:
        try:
            # DB Connection
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="main"
            )
            cursor = connection.cursor()
            # Create DB
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usersflask (
                    id INT(11) NOT NULL AUTO_INCREMENT,
                    name VARCHAR(255),
                    email VARCHAR(255) UNIQUE,
                    password VARCHAR(255),
                    PRIMARY KEY (id)  
                )"""
                )
            # Check if user email is already registered
            cursor.execute("SELECT email FROM usersflask WHERE email = %s", (email,))
            existing_email = cursor.fetchone()
            # Hash user password
            def hashPw(password):
                    global hashed_pw
                    pw = str(password)
                    encoded = pw.encode()
                    salt = bcrypt.gensalt()
                    hashed_pw = bcrypt.hashpw(encoded, salt)

            # Register system
            if existing_email:
                print('Email already registered')
            else:
                hashPw(pw1)
                cursor.execute("INSERT INTO usersflask (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_pw))
                connection.commit()
                print('User registered')

            connection.close() 


        except Error as erro:
                print(f'Erro ao inserir dados no MySQL: {erro}')

def login(email, password):
    if email and password:
        try:
             # DB Connection
            database = mysql.connector.connect(
                host="127.0.0.1",  # Substitua pelo endereço do servidor MySQL
                user="root",       # Substitua pelo usuário do MySQL
                password="",  # Substitua pela senha do MySQL
                database="main"  # Substitua pelo nome do banco de dados
            )
            cursor = database.cursor()
            # Catch user password from database
            cursor.execute("SELECT password FROM usersflask WHERE email = %s", (email,))
            password_bd = cursor.fetchone()

            database.close()
            if bcrypt.checkpw(password=password.encode(), hashed_password=password_bd[0].encode()) == True:
                print('login successfull')
            else:
                print('incorrect credentials')

        except Error as erro:
            print(f'Erro ao conectar ou consultar no MySQL: {erro}')
