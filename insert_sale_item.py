import sqlite3

def sale_item_insert(conn):


    conn.execute(
        "INSERT INTO sale_items(sale_item_id,sale_id,product_id,quantity,unit_cents) VALUES(?,?,?,?,?)",
        (1,1001,1,2,"350")
    )
    conn.commit()
    print("One Sale Item Added")


    conn.executemany(
        "INSERT INTO sale_items(sale_item_id,sale_id,product_id,quantity,unit_cents) VALUES(?,?,?,?,?)",
        [
            (2,1001,2,1,"220"),
            (3,1002,3,2,"250"),
            (4,1003,4,1,"450"),
            (5,1003,5,2,"100")
        ]
    )
    conn.commit()
    print("Multiple Sale Items Added")    