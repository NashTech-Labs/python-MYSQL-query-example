import sqlite3

def execute_sqlite_query(database_file, query):
    try:
        # Connect to the database
        connection = sqlite3.connect(database_file)

        # Execute the query
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close the connection
        connection.close()

    except Exception as e:
        print(f"An error occurred while executing the database query: {e}")

# Example usage
database_file = "database.db"
database_query = "SELECT * FROM users"
execute_sqlite_query(database_file, database_query)

