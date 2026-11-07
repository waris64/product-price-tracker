import sqlite3 
connection = sqlite3.connect('price_tracker.db')
print('Database created Successfully ')
connection.close()