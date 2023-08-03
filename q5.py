import mysql.connector
import csv

csv_file = "file.csv"
db = "database_name"

hostname = "localhost"
username = "username"

# ler o arquivo CSV
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    header = next(reader) # guardar o header do arquivo

    data = [tuple(linha) for linha in reader] #  guardar os dados

try:
    conn = mysql.connector.connect(host=hostname, database=db, user=username)
    cursor = conn.cursor()

    # criar a tabela
    query = f"CREATE TABLE IF NOT EXISTS stg_paciente.Procedimento_Medico ({', '.join(header)})"
    cursor.execute(query)

    # inserir os dados na tabela
    query = f"INSERT INTO stg_paciente.Procedimento_Medico ({', '.join(header)}) VALUES ({', '.join(['%s']*len(header))})"
    cursor.execute(query, data)

    conn.commit()

except mysql.connector.Error as erro:
    print("Erro ao executar opercao: {}".format(erro))
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("Conexao finalizada")