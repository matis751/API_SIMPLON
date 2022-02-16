import pymysql

host, user, password, charset, db = '127.0.0.1', 'root', '1234', 'utf8mb4', 'db_api'

# Connection à l'instance de la database
def connect_to_instance_db():
    try:
        conn = pymysql.connect(
                host=host,
                user=user,
                password=password,
                charset=charset)
    except pymysql.err.OperationalError as e:
        raise e
    else:
        print("Connection Successful!")
    return conn, conn.cursor()

# Création de la database
def create_db():
    conn, cursor = connect_to_instance_db()
    if cursor:
        queries = (
            f"DROP DATABASE IF EXISTS {db}",
            f"CREATE DATABASE {db}",
            f"USE {db}"
        )
        
        for query in queries:
            cursor.execute(query)
            conn.commit()

# Création des tables
def create_table():
    conn, cursor = connect_to_instance_db()
    queries = (
    f"USE {db}",
    "DROP TABLE IF EXISTS title",
    ''' CREATE TABLE title(
        id INT,
        name VARCHAR(50),
        url VARCHAR(50),
        PRIMARY KEY(id))''',
    
    "DROP TABLE IF EXISTS hashage",
    ''' CREATE TABLE hashage(
        id INT,
        word TEXT,
        occurence INT,
        id_1 INT NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY(id_1) REFERENCES title(id))''')
    
    for query in queries:
        cursor.execute(query)
        conn.commit()

create_db()
create_table()