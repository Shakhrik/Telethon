import psycopg2
import config

def dbConnection():
    try:
        con = psycopg2.connect(
            database = config.POSTGRES_DATABASE,
            user = config.POSTGRES_USER,
            password = config.POSTGRES_PASSWORD, 
            host = config.POSTGRES_HOST, 
            port= config.POSTGRES_PORT
        )
        return con
    except Exception as e:
        print("Error while connecting to the database...", e)

def dbReader(con):
    try:
        cursor = con.cursor()
        query = '''select r.name_uz,count(1) as registered_users, r.id as region_id, (select count(1) from customers where active = true)  from customers c
            join regions r on (c.address -> 'region' ->>'id')::NUMERIC = r.id
            where c.active = true
            group by r.name_uz, r.id order by r.id asc'''
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("Error while getting data from database..", e)

        