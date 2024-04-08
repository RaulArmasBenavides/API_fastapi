
from abc import ABC,abstractmethod
from typing import List

from core.models.entry import EntryModel


class IEntryRepository(ABC):
    @abstractmethod
    def add_entry(self, entry: EntryModel) -> EntryModel:
        pass

    @abstractmethod
    def view_entries(self) -> List[EntryModel]:
        pass

    @abstractmethod
    def delete_entry(self, entry_id: int) -> None:
        pass