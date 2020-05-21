import pyrebase
from dotenv import load_dotenv
import os
from datetime import datetime
import json
import random
import copy
load_dotenv()
config = {
    "apiKey": "apiKey",
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DB_URL"),
    "storageBucket":  os.getenv("STORAGE_BUCKET"),
}

firebase = pyrebase.initialize_app(config)

# db = firebase.database()
# data = db.child("formData")
# # data_loc = db.child("formData")


def get_note_amt(data_in):
    return len(data_in.each())


def get_notes_iterable(data_in):
    iter = {}
    for note in data_in.each():
        iter[note.key()] = note.val()
    return iter


"""
condition is the parameter (approved, sent)
value is the boolean value (true, false, or an exact string)
"""


def get_note_condition(data_in, condition, value):
    iter = {}
    for note in data_in.each():
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


"""
pass in data location (child)
the list of children of that location
the param to set
and what to set it to
"""


def set_notes_value(data_location, key_list, param, value):
    for key in key_list:
        temp_ref = copy.copy(data_location)
        temp_ref.child(key).update({param: random.choice(value)})


# NOTE: DO NOT REMOVE LINE!
if not os.path.isdir('./backup_data'):
    os.mkdir('backup_data')
open('backup_data/'+datetime.now().strftime("%m%d%Y-%H%M%S") +
     '.json', 'w+').write(json.dumps(get_notes_iterable(firebase.database().child("formData").get())))

# NOTE: ALL CODE BELOW THIS POINT
