import pyrebase

# Configure Firebase
config = {
    "apiKey": "AIzaSyAaiWFa_Ohf1W3FbRKssvtzG4njIeq2fpY",
    "authDomain": "inshortsnewsapk.firebaseapp.com",
    "databaseURL": "https://inshortsnewsapk-default-rtdb.europe-west1.firebasedatabase.app",
    "storageBucket": "inshortsnewsapk.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the database
db = firebase.database()

# Define the data you want to insert
data = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com"
}

# Insert the data into the database
db.child("users").push(data)

print("Data inserted successfully!")
