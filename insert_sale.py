import sqlite3

def sale_insert(conn):

    conn.execute(
        "INSERT INTO sales(sale_id,customer_id,employee_id,sale_date,total_cents) VALUES(?,?,?,?,?)",
        (1001,1,1,"2026-10-20","920")
    )
    conn.commit()
    print("One Sale Added")


    conn.executemany(
        "INSERT INTO sales(sale_id,customer_id,employee_id,sale_date,total_cents) VALUES(?,?,?,?,?)",
        [
            (1002,2,2,"2026-10-20","500"),
            (1003,3,3,"2026-10-20","650")
        ]
    )
    conn.commit()
    print("Multiple Sales Added")    