
(1) PostgreSQL Python -> https://www.postgresqltutorial.com/postgresql-python/.

Python has various database drivers for PostgreSQL. Currently, the psycopg is the most popular PostgreSQL database adapter for the Python language. The psycopg fully implements the Python DB-API 2.0 specification.

The current version of the psycopg is 2 or psycopg2. The psycopg2 database adapter implemented in C as a libpq wrapper resulting in both fast and secure. The psycopg2 provides many useful features such as client-side and server-side cursors, asynchronous notification and communication, COPY command support, etc.

Besides, the psycopg2 driver supports many Python types out-of-the-box. The psycopg2 matches Python objects to the PostgreSQL data types, e.g., list to the array, tuples to records, and dictionary to hstore.  If you want to customize and extend the type adaption, you can use a flexible object adaption system.

(2) Example database.

For demonstration purposes, we will use the suppliers sample database. The following picture illustrates the structure of the suppliers database:

    'PostgreSQL-Python-Sample-Database-Diagram.png'
    
The suppliers database has the following tables:

    'vendors' table : stores vendor data.
    'parts' table : stores parts data.
    'parts_drawings' table : stores the drawing of a part.
    'vendor_parts' table : stores the data of which parts supplied by which vendor.

(3) Install the psycopg2 module.

Use the following command line from the terminal:

    pip install psycopg2

