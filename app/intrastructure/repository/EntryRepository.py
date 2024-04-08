import datetime
from typing import List
from peewee import * 
from collections import OrderedDict
from core.interfaces.IEntryRepository import IEntryRepository
from core.models.entry import EntryModel

db = SqliteDatabase('diary.db')

menu_items = OrderedDict([
    ('a','addentry'),
    ('v','view entry'),
    ('d','delete entry')
])

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)

    class Meta: 
        database = db


class  EntryRepository(  IEntryRepository):
    def add_entry(self, entry: EntryModel) -> EntryModel:
        with db.atomic():
            peewee_model = Entry.create(content=entry.content)
            return EntryModel(id=peewee_model.id, content=peewee_model.content, timestamp=peewee_model.timestamp)

    def view_entries(self) -> List[EntryModel]:
        entries = Entry.select()
        return [EntryModel(id=e.id, content=e.content, timestamp=e.timestamp) for e in entries]

    def delete_entry(self, entry_id: int) -> None:
        entry = Entry.get(Entry.id == entry_id)
        entry.delete_instance()


def create_and_connect():
        """Conecta a la base de datos y crea las tablas si no existen."""
        db.connect()
        db.create_tables([Entry], safe=True)
    