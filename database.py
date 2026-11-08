import sqlite3 
connection = sqlite3.connect('price_tracker.db')
# Enable foreign key validation
connection.execute("PRAGMA foreign_keys = ON")
# create the products table
connection.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    current_price REAL NOT NULL, 
    availability TEXT DEFAULT 'Unknown',
    rating REAL DEFAULT 0.0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
# INSERTING THE VALUES IN THE COLUMNS
# inserted = connection.execute(""" 
# INSERT INTO products(id,name,url,current_price,availability,rating) VALUES (1,'Samsung A55','https://example.com/samsung-a55' , 115000,'In Stock',4.5)
# """)
#CREATE PRICE HISTORY TABLE 
connection.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER primary key,
            product_id INTEGER NOT NULL,
            price REAL NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(id))
""")
connection.commit()
cursor =  connection.execute(
"""
SELECT name
FROM sqlite_master
WHERE type = 'table' 
AND name NOT LIKE 'sqlite_%'   
""")
result = cursor.fetchall()
print("Result = " ,result)
print("Tables created successfully")
    # retrives the every column from the products
gettingProducts = connection.execute(
    """
    SELECT * FROM products
    """
    )
res = gettingProducts.fetchall();
print("All products :",res)
tableInfo = connection.execute("""PRAGMA table_info(products)""")
productsFetched = tableInfo.fetchall()
print("Checking result: ", productsFetched)
connection.close()