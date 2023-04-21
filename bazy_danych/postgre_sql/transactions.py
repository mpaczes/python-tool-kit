
import psycopg2

def add_part(part_name, vendor_list):
    # statement for inserting a new row into the parts table
    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"

    # statement for inserting a new row into the vendor_parts table
    assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)"

    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5455",
            database="suppliers",
            user="postgres",
            password="postgres")
        cur = conn.cursor()
        # insert a new part
        cur.execute(insert_part, (part_name,))
        # get the part id
        part_id = cur.fetchone()[0]
        # assign parts provided by vendors
        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Transactions using the with statement
# Starting from psycopg 2.5, the connection and cursor are Context Managers and therefore you can use them with the with statement.
#
# Psycopg commits the transaction if no exception occurs within the with block, and otherwise it rolls back the transaction.
#
# Unlike other context manager objects, exiting the with block does not close the connection but only terminates the transaction. As a result, you can use the same connection object in the subsequent with statement in another transaction.
def add_part_with_context_managers(part_name, vendor_list):
    # statement for inserting a new row into the parts table
    insert_part = "INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"
    
    # statement for inserting a new row into the vendor_parts table
    assign_vendor = "INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)"

    conn = None
    part_id = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5455",
            database="suppliers",
            user="postgres",
            password="postgres")

        # transaction 1
        with conn:
            with conn.cursor() as cur:
                # insert a new part
                cur.execute(insert_part, (part_name,))
                # get the part id
                part_id = cur.fetchone()[0]

        # transaction 2
        with conn:
            with conn.cursor() as cur:
                # assign parts provided by vendors
                for vendor_id in vendor_list:
                    cur.execute(assign_vendor, (vendor_id, part_id))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # add_part('SIM Tray', (1, 2))
    # add_part('Speaker', (3, 4))
    # add_part('Vibrator', (5, 6))
    # add_part('Antenna', (6, 7))
    # add_part('Home Button', (1, 5))
    # add_part('LTE Modem', (1, 5))

    add_part_with_context_managers('SIM Tray', (1, 2))
    add_part_with_context_managers('Speaker', (3, 4))
    add_part_with_context_managers('Vibrator', (5, 6))
    add_part_with_context_managers('Antenna', (6, 7))
    add_part_with_context_managers('Home Button', (1, 5))
    add_part_with_context_managers('LTE Modem', (1, 5))
