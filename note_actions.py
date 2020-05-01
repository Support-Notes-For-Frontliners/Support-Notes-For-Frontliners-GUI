import pyrebase
from dotenv import load_dotenv
import os
from datetime import datetime
import json
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


def update_notes(data_location, updated_data):
    for key, value in updated_data.items():
        data_location.child(key).set(value)


# NOTE: DO NOT REMOVE LINE!
if not os.path.isdir('./backup_data'):
    os.mkdir('backup_data')
open('backup_data/'+datetime.now().strftime("%m%d%Y-%H%M%S") +
     '.json', 'w+').write(json.dumps(get_notes_iterable(data)))

# NOTE: ALL CODE BELOW THIS POINT

# print(update_notes(data_loc, get_notes_iterable(data)))
