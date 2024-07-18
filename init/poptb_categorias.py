from faker import Faker
import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados MySQL
db_config = {
    'host': 'localhost',
    'database': 'db_cbook',
    'user': 'root',
    'password': '',  # Deixe a senha vazia
    'port': 3307
}

# Função para inserir dados aleatórios na tabela
def insert_random_data(connection, cursor):
    fake = Faker()
    for _ in range(4):  # Inserir 4 registros
        nome_categoria = fake.text()
        
        # Query SQL para inserção de dados
        insert_query = f"INSERT INTO tb_categorias (nome_categoria) " \
                       f"VALUES ('{nome_categoria}')"

        try:
            cursor.execute(insert_query)
            connection.commit()
        except Error as e:
            print(f"Erro ao inserir dados: {e}")

# Função principal para conexão e execução do script
def main():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()

            # Chamada para inserção de dados
            insert_random_data(connection, cursor)

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL foi encerrada.")

if __name__ == '__main__':
    main()
