 


from typing import List
from core.models.entry import EntryModel
from intrastructure.repository.EntryRepository import EntryRepository


class EntryService:
    def __init__(self, repository: EntryRepository):
        self.repository = repository

    def create_entry(self, entry_data: EntryModel) -> EntryModel:
        return self.repository.add_entry(entry_data)

    def get_entries(self) -> List[EntryModel]:
        return self.repository.view_entries()

    def remove_entry(self, entry_id: int) -> None:
        self.repository.delete_entry(entry_id)