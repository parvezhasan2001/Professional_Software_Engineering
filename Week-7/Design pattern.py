#Week- 7 Activity-1

#Description: creating a get_db_connection function to connect to a database and two service classes, UserService and OrderService, that use this function to fetch user and order data respectively. improving code reusability and maintainability.

import sqlite3
 
def get_db_connection():
    conn = sqlite3.connect('app.db')
    return conn

class UserService:
    def get_user(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result
 
class OrderService:
    def get_orders(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result