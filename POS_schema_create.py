import sqlite3

def pos_create_schema():
    conn = sqlite3.connect("Shop_POS_system.db")
    print("Connected")

    category_schema ="""
    CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL
    )
    """

    conn.execute(category_schema)
    print("Category Schema Created")


    product_schema ="""
    CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    price_cents TEXT NOT NULL,
    stock TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
    )
    """

    conn.execute(product_schema)
    print("Product Schema Created")


    customer_schema ="""
    CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email TEXT NOT NULL
    )
    """

    conn.execute(customer_schema)
    print("Customer_Schema_Created")


    employee_schema ="""
    CREATE TABLE IF NOT EXISTS employees(
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    role TEXT NOT NULL
    )
    """

    conn.execute(employee_schema)
    print("Employee Schema Created")


    sale_schema ="""
    CREATE TABLE IF NOT EXISTS sales(
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    sale_date TEXT NOT NULL,
    total_cents TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
    """

    conn.execute(sale_schema)
    print("Sale Schema Created")


    sale_item_schema ="""
    CREATE TABLE IF NOT EXISTS sale_items(
    sale_item_id INTEGER PRIMARY KEY,
    sale_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_cents TEXT NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """

    conn.execute(sale_item_schema)
    print("Sale Item Schema Created")
    return conn

    conn.execute(category_schema)
    conn.execute(product_schema)
    conn.execute(customer_schema)
    conn.execute(employee_schema)
    conn.execute(sale_schema)
    conn.execute(sale_item_schema)
    conn.commit()

    print("DATABASE CONNECTED")