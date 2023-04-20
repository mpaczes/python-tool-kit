import psycopg2     # A Python driver for PostgreSQL

# Baze danych mam w kontenerze Dockera :
#       docker pull postgres:14.5
#       docker run --name postgres__14_5 -p 5455:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=suppliers -d postgres:14.5

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host="localhost",
            port="5455",
            database="suppliers",
            user="postgres",
            password="postgres")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()

# How it works.
#
# Next, create a new database connection by calling the connect() function.
# Then, create a new cursor and execute an SQL statement to get the PostgreSQL database version.
# After that, read the result set by calling the  fetchone() method of the cursor object.
# Finally, close the communication with the database server by calling the close() method of the cursor and connection objects.

# Execute the connect.py file
# To execute the connect.py file, you use the following command: 
#       python connect.py

# You will see the following output:
#
#       Connecting to the PostgreSQL database...
#       PostgreSQL database version:
#       ('PostgreSQL 14.5 (Debian 14.5-2.pgdg110+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit',)
#       Database connection closed.

# It means that you have successfully connected to the PostgreSQL database server.
