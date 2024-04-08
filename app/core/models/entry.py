from pydantic import BaseModel
import datetime

class EntryModel(BaseModel):
    id: int = 0
    content: str
    timestamp: datetime.datetime = datetime.datetime.now()