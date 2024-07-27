import yaml
import mysql.connector
from sqlalchemy import create_engine, URL

print('Initializing variables')
with open('docker-compose.yaml', 'r') as creds_file:
    creds_db = yaml.safe_load(creds_file)['services']['atm-db']['environment']
    db_name = "atm-db"
    db_user = 'root'
    db_pw = creds_db['MYSQL_ROOT_PASSWORD']

transaction_table = """
                    CREATE TABLE IF NOT EXIST ATM.TRANSACTIONS
                    (   STAMP DATETIME,
                        TRANSACTION_ID INT,
                        ATM_ID SMALLINT
                        BANK_NAME VARCHAR(74),
                        ACCOUNT_NUMBER BIGINT,
                        TRANSACTION_VALUE SMALLINT);
                """
# host.docker.internal
print("Connecting to the database")
try:
    print(db_name)
    print(db_user)
    print(db_pw)
    url_object = URL.create(
        "mysql+pymysql",
        username="root",
        password="set-your-password",  # plain (unescaped) text
        host="mysql",
        database="atm-db",
    )
    engine = create_engine(url_object)
    #connection = mysql.connector.connect(host="mysql://atm-db", database="atm-db", user=db_user, password=db_pw)
    print("Connected to database")
except Exception as e:
    print("Error: ", e)
    exit()

cursor = connection.cursor()
print("Creating table")
result = cursor.execute(transaction_table)
print(result)

print("selecting table")
result2 = cursor.execute("SELECT * FROM ATM.TRANSACTIONS")
print(result2)