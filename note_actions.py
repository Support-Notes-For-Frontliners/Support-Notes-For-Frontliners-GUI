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


print(get_note_condition(data,'sent',True))