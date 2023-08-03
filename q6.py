import mysql.connector
import requests


db = "database_name"
hostname = "localhost"
username = "username"

api_url = "api_url"

resposta = requests.get(api_url)


try:
    resposta.raise_for_status()
except requests.exceptions.HTTPError as erro:
    print("Erro: " + erro)
finally:
    data = resposta.json();

    if not data:
        print("Nao ha dados.")
        exit()
    
    colunas = list(data[0].keys())

    try:

        conn = mysql.connector.connect(host=hostname, database=db, user=username)
        cursor = conn.cursor()

        # criar a tabela
        query = f"CREATE TABLE IF NOT EXISTS stg_paciente.Procedimento_Medico ({', '.join(colunas)})"
        cursor.execute(query)

        # inserir os dados na tabela
        query = f"INSERT INTO stg_paciente.Procedimento_Medico ({', '.join(colunas)}) VALUES ({', '.join(['%s']*len(colunas))})"
        
        data_to_insert = [[item[col] for col in colunas] for item in data]
        cursor.execute(query, data_to_insert)
        conn.commit()

    except mysql.connector.Error as erro:
        print("Erro ao executar opercao: {}".format(erro))
    finally:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print("Conexao finalizada")