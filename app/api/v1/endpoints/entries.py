from fastapi import APIRouter
from dependency_injector.wiring import Provide, inject
from app.application.services.EntryService import EntryService
from app.core.models.entry import EntryModel

router = APIRouter(
    prefix="/entries",
    tags=["entries"],
)
@router.get("/test")
@inject
async def read_root():
    return {"message": "Bienvenido a mi API construida con FastAPI!"}
# repository =  EntryRepository()
# service = EntryService(repository)

# @router.post("/entries/", response_model=EntryModel)
# async def create_entry(entry_data: EntryModel):
#     return service.create_entry(entry_data)

@router.get("/entries/", response_model=List[EntryModel])
async def get_entries():
    return service.get_entries()

# @router.delete("/entries/{entry_id}")
# async def delete_entry(entry_id: int):
#     service.remove_entry(entry_id)
#     return {"message": "Entry deleted"}