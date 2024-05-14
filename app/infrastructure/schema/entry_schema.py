from peewee import SqliteDatabase,Model,TextField,DateTimeField 
import datetime
db = SqliteDatabase('diary.db')

class EntrySchema(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)

    class Meta: 
        database = db
