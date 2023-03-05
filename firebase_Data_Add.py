import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

print(firebase_admin)
"""
# Initialize the Firebase app with your credentials
cred = credentials.Certificate('inshortsnewsapk-7faf16b82547.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://inshortsnewsapk-default-rtdb.europe-west1.firebasedatabase.app'
})

# Get a reference to the Firebase Realtime Database
ref = db.reference('https://inshortsnewsapk-default-rtdb.europe-west1.firebasedatabase.app')

# Add data to the database as key-value pairs
ref.update({
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
})
"""