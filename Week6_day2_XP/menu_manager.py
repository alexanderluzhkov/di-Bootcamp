import psycopg2
from menu_item import MenuItem 

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        connection = psycopg2.connect(database="restaurant_menu", user="postgres", password="Begemotik")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (name,))
        item = cursor.fetchone()
        cursor.close()
        connection.close()
        if item:
            return MenuItem(item[1], item[2])
        return None

    @classmethod
    def all_items(cls):
        connection = psycopg2.connect(database="restaurant_menu", user="postgres", password="Begemotik")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Menu_Items")
        items = cursor.fetchall()
        cursor.close()
        connection.close()
        return [MenuItem(item[1], item[2]) for item in items]
