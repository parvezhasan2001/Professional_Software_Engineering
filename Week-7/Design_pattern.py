#Week-7 Activity-2

#Description: create a singleton database connection class and two service classes that use this connection to perform database operations.

import sqlite3
from db import DatabaseConnection
    
class UserService:
    
    def __init__(self):
        self.db = DatabaseConnection()

    def get_user(self, user_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        return result
 
class OrderService:

    def __init__(self):
        self.db = DatabaseConnection()

    def get_orders(self, user_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        return result