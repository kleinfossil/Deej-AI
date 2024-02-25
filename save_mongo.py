from pymongo import MongoClient


def save_to_mongo(playlist, output):

    # Connect to the MongoDB client
    client = MongoClient('mongodb://localhost:27017/')

    # Select the database
    db = client['musicdb']

    # Select the collection
    collection = db['ai_playlist_data']

    # Convert the list to a dictionary
    playlist_document = {'playlist': playlist, 'file_path': output}

    # Insert the document into the collection
    collection.insert_one(playlist_document)
