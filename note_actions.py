import pyrebase
from dotenv import load_dotenv
import os
load_dotenv()

config = {
    "apiKey": "apiKey",
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DB_URL"),
    "storageBucket":  os.getenv("STORAGE_BUCKET"),
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
data = db.child("formData").get()
data_loc = db.child("formData")


def get_note_amt(data):
    return len(data.each())


def get_notes_iterable(data):
    iter = {}
    for note in data.each():
        iter[note.key()] = note.val()
    return iter


"""
condition is the parameter (approved, sent)
value is the boolean value (true, false, or an exact string)
"""


def get_note_condition(data, condition, value):
    iter = {}
    for note in data.each():
        if note.val()[condition] == value:
            iter[note.key()] = note.val()
    return iter


"""
Pass in the data_loc and the all the values passed in update_data
format of updated_data
{
  'uniquekey': noteData
}
"""


def update_notes(data_loc, updated_data):
    for key, value in updated_data.items():
        data_loc.child(key).set(value)
