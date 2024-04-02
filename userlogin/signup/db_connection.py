
# from pymongo import MongoClient
# from django.conf import settings

# class MongoDBConnection:
#     def __init__(self):
#         self.client = MongoClient(host=settings.MONGODB_DATABASES['default']['HOST'],
#                                   port=settings.MONGODB_DATABASES['default']['PORT'])

#         self.db = self.client[settings.MONGODB_DATABASES['default']['NAME']]

# mongodb_connection = MongoDBConnection()


#                      ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from pymongo import MongoClient

def mongodb_connection():
    try:
        # Connect to MongoDB server
        client = MongoClient('mongodb://localhost:27017/')
        
        # Access the desired database
        db = client['userlogin']
        
        # Access the desired collection
        collection = db['userdetails']
        
        # You can also create a context manager for handling connections and disconnections
        ctx = client.start_session()
        
        # Return the necessary MongoDB objects
        return client, collection, ctx
    
    except Exception as e:
        # Handle connection errors
        print(f"Error connecting to MongoDB: {e}")
        return None, None, None