from peewee import SqliteDatabase,Model,TextField,DateTimeField 
import datetime
from .db import db_proxy

class EntrySchema(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)

    class Meta: 
        database = db_proxy
