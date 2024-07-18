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
    for _ in range(1000):  # Inserir 1000 registros
        nome = fake.name()
        email = fake.email()
        telefone = fake.phone_number()
        data_criacao = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
        descricao = fake.text()
        categoria = fake.random_int(min=1, max=4)  # Ajuste o intervalo conforme necessário

        # Query SQL para inserção de dados
        insert_query = f"INSERT INTO tb_dados (nome, email, telefone, data_criacao, descricao, categoria) " \
                       f"VALUES ('{nome}', '{email}', '{telefone}', '{data_criacao}', '{descricao}', {categoria})"

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
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL foi encerrada.")

if __name__ == '__main__':
    main()
