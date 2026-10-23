import sqlite3

def employee_insert(conn):

    conn.execute(
        "INSERT INTO employees(employee_id,employee_name,role) VALUES(?,?,?)",
        (1,"Maya","Cashier")        
    )
    conn.commit()
    print("One Employee Added")


    conn.executemany(
        "INSERT INTO employees(employee_id,employee_name,role) VALUES(?,?,?)",
        [
            (2,"Leo","Manager"),
            (3,"Nina","Cashier")
        ]        
    )
    conn.commit()
    print("Multiple Employees Added")   