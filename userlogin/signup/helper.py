import bcrypt
from .db_connection import mongodb_connection

def signup_user(name, email, password, number):
    try:
        client, collection, ctx = mongodb_connection()
        if not collection:
            return False, "Error connecting to database"
        
        existing_user = collection.find_one({"email": email})
        if existing_user:
            return False, "User with this email already exists" 
        
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        user_data = {
            "name": name,
            "email": email,
            "password": hashed_password,
            "number": number,
            "status": 1
        }

        collection.insert_one(user_data)
        ctx.end_session()
        client.close()
        return True, "User inserted successfully"
    except Exception as e:
        print("Error:", e)
        return False, "Error in user registration"
