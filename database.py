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
"""SELECT name
FROM sqlite_master
WHERE type = 'table' 
AND name NOT LIKE 'sqlite_%'   
""")
result = cursor.fetchall()
print("Result = " ,result)
print("Tables created successfully")

connection.close()