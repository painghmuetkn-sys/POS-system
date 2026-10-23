import sqlite3

def category_insert(conn):

    conn.execute(
        "INSERT INTO categories(category_id,category_name) VALUES(?,?)",
        (1,"Drinks")
    )
    conn.commit()
    print("One Category Added")


    conn.executemany(
        "INSERT INTO categories(category_id,category_name) VALUES(?,?)",
        [
            (2,"Food"),
            (3,"Stationery")
        ]
    )
    conn.commit()
    print("Multiple Categories Added")   