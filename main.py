import sqlite3 # database import
# Function to create a table
def create_table():
    connection = sqlite3.connect("data.db")  # "conn" is a object which represent the connection to sqlite db file("items.db")
    # cursor allows to interact the database by executing SQL queries.
    cursor = connection.cursor()  # created curser object to connect with databases.

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

# Function to insert a new item.
def insert_item(name):
    connection = sqlite3.connect("data.db") # Connect to the database
    cursor = connection.cursor()

    cursor.execute("INSERT INTO items (name) VALUES (?)", (name,))

    connection.commit()
    connection.close()

# Function to read all items.
def read_items():
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    connection.close()

    return items

# Function to update an item.
def update_item(item_id, new_name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE items SET name=? WHERE id=?", (new_name, item_id))

    connection.commit()
    connection.close()

# Function to delete an item.
def delete_item(item_id):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM items WHERE id=?", (item_id,))

    connection.commit()
    connection.close()

# Main function to interact with the user.
if __name__ == "__main__":
    create_table() # Create a table to store items if it doesn't exist, each table is created with 2 parts "id" and "items"

    while True:
        print("\nChoose an option:")
        print("1. Add an item")
        print("2. View all items")
        print("3. Update an item")
        print("4. Delete an item")
        print("5. Exit")

        pick_item = int(input("Enter your choice (1-5): "))

        if pick_item == 1:
            name = input("Enter the item name: ")
            insert_item(name)
            print("Item added successfully!")

        elif pick_item == 2:
            items = read_items()
            print("Items:")
            for item in items:
                print(f"{item[0]}. {item[1]}")

        elif pick_item == 3:
            item_id = int(input("Enter the item ID to update: "))
            new_name = input("Enter the new item name: ")
            update_item(item_id, new_name)
            print("Item updated successfully!")

        elif pick_item == 4:
            item_id = int(input("Enter the item ID to delete: "))
            delete_item(item_id)
            print("Item deleted successfully!")

        elif pick_item == 5:
            print(" Come Again,Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
