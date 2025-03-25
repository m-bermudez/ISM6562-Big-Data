from quickstart_connect import connect_to_database

def filter_books_cql():
    # Connect to Astra DB using Cassandra driver
    session = connect_to_database()

    # Execute CQL query
    query = "SELECT title, rating FROM books WHERE rating >= 4.0 ALLOW FILTERING;"
    rows = session.execute(query)

    # Print results
    for row in rows:
        print(f"Title: {row.title}, Rating: {row.rating}")

# Run the function
filter_books_cql()
