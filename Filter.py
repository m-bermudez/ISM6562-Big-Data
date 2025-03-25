from quickstart_connect import connect_to_database

def filter_books_by_rating(min_rating=4.0):
    # Connect to Astra DB
    db = connect_to_database()

    # Use get_collection instead of collection()
    books_collection = db.get_collection("quickstart_collection")

    # Query books with rating >= min_rating
    filtered_books = books_collection.find({"rating": {"$gte": min_rating}})

    # Print results
    for book in filtered_books:
        print(f"Title: {book['title']}, Rating: {book['rating']}")

# Run the filtering function
filter_books_by_rating()
