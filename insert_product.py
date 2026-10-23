import sqlite3

def product_insert(conn):

    conn.execute(
        "INSERT INTO products(product_id,product_name,category_id,price_cents,stock) VALUES(?,?,?,?,?)",
        (1,"Coffee",1,"350","40")
    )
    conn.commit()
    print("One Product Added")


    conn.executemany(
        "INSERT INTO products(product_id,product_name,category_id,price_cents,stock) VALUES(?,?,?,?,?)",
        [
            (2,"Milk",1,"220","25"),
            (3,"Bread",2,"250","20"),
            (4,"Notebook",3,"450","30"),
            (5,"Pen",3,"100","60")
        ]
    )
    conn.commit()
    print("Multiple Products Added")    