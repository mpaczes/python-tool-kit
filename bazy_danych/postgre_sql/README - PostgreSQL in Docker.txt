
How to Use the Postgres Docker Official Image -> https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/

(1) How to run Postgres in Docker.

    docker pull postgres:14.5       # wersja postgres v14.5

(2) Start a Postgres instance.

    docker run --name postgres__14_5 -p 5455:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=suppliers -d postgres:14.5
    
    # docker run --name postgres__14_5 -e POSTGRES_PASSWORD=postgres -d postgres:14.5

(3) Extending your Postgres image -> Environment variables.


    There are many ways to customize or configure your Postgres image. Let’s tackle four important mechanisms that can help you.
    
    
    We’ve touched briefly on the importance of POSTGRES_PASSWORD to Postgres. Without specifying this, Postgres can’t run effectively. But there are also other variables that influence container behavior: 

        POSTGRES_USER – Specifies a user with superuser privileges and a database with the same name. Postgres uses the default user when this 
        is empty.
        
        POSTGRES_DB – Specifies a name for your database or defaults to the 
        POSTGRES_USER value when left blank. 
        
        POSTGRES_INITDB_ARGS – Sends arguments to postgres_initdb and adds functionality
        
        POSTGRES_INITDB_WALDIR – Defines a specific directory for the Postgres transaction log. A transaction is an operation and usually describes a change to your database. 
        
        POSTGRES_HOST_AUTH_METHOD – Controls the auth-method for host connections to all databases, users, and addresses
        
        PGDATA – Defines another default location or subdirectory for database files
