import sqlite3

def customer_insert(conn):

    conn.execute(
        "INSERT INTO customers(customer_id,customer_name,email) VALUES(?,?,?)",
        (1,"Ana","ana@example.com")
    )
    conn.commit()
    print("One Customer Added")


    conn.executemany(
        "INSERT INTO customers(customer_id,customer_name,email) VALUES(?,?,?)",
        [
            (2,"Ben","ben@example.com"),
            (3,"Cara","cara@example.com")
        ]
    )
    conn.commit()
    print("Multiple Customers Added")    