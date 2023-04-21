# The  fetchone() fetches the next row in the result set. It returns a single tuple or None when no more row is available.
# The  fetchmany(size=cursor.arraysize) fetches the next set of rows specified by the size parameter. If you omit this parameter, the  arraysize will determine the number of rows to be fetched. The  fetchmany() method returns a list of tuples or an empty list if no more rows available.
# The  fetchall() fetches all rows in the result set and returns a list of tuples. If there are no rows to fetch, the  fetchall() method returns an empty list.

import psycopg2

# The following get_vendor() function selects data from the vendors table and fetches the rows using the  fetchone() method.
def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5455",
            database="suppliers",
            user="postgres",
            password="postgres")
        cur = conn.cursor()
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# if __name__ == '__main__':
#     get_vendors()

# The following get_parts() function uses the fetchall() method of the cursor object to fetch rows from the result set and displays all the parts in the parts table.
def get_parts():
    """ query parts from the parts table """
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5455",
            database="suppliers",
            user="postgres",
            password="postgres")
        cur = conn.cursor()
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# if __name__ == '__main__':
#     get_parts()

# The following get_suppliers() function selects parts and vendors data using the fetchmany() method.
def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_part_vendors():
    """ query part and vendor data from multiple tables"""
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5455",
            database="suppliers",
            user="postgres",
            password="postgres")
        cur = conn.cursor()
        cur.execute("""
            SELECT part_name, vendor_name
            FROM parts
            INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
            INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
            ORDER BY part_name;
        """)
        for row in iter_row(cur, 10):
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_part_vendors()
