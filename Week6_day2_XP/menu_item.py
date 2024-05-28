import psycopg2

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        connection = psycopg2.connect(database="restaurant_menu", user="postgres", password="Begemotik")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)", (self.item_name, self.item_price))
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self):
        connection = psycopg2.connect(database="restaurant_menu", user="postgres", password="Begemotik")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.item_name,))
        connection.commit()
        cursor.close()
        connection.close()

    def update(self, new_name, new_price):
        connection = psycopg2.connect(database="restaurant_menu", user="postgres", password="Begemotik")
        cursor = connection.cursor()
        cursor.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s", (new_name, new_price, self.item_name))
        connection.commit()
        cursor.close()
        connection.close()
