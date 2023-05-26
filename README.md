# Execute a database query using SQLite database in Python

This script demonstrates how to execute a database query using the SQLite database and the sqlite3 module, which is a built-in module in Python for working with SQLite databases.

The execute_sqlite_query function takes two parameters: database_file (the path to the SQLite database file) and query (the SQL query to execute).
Inside the function, we connect to the SQLite database using the connect function from sqlite3. This establishes a connection to the database file.
We then create a cursor object using connection.cursor(). The cursor allows us to execute SQL commands and fetch results from the database.
The query is executed using cursor.execute(query), where query is the SQL query provided as a parameter to the function.
We fetch the results using cursor.fetchall(), which returns all the rows returned by the query.
Finally, we iterate over the rows and print them.
The connection is closed using connection.close() to release the resources.

