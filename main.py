# Importa FastAPI
from typing import List
from fastapi import FastAPI

from application.services.EntryService import EntryService
from core.models.entry import EntryModel
from intrastructure.repository.EntryRepository import EntryRepository, create_and_connect,db

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

 
# @app.on_event("startup") 
# # @app.router.lifecycle.on_startup()
# def startup_event():
#     """Evento de inicio para realizar tareas iniciales como la conexión a la base de datos."""
#     create_and_connect()

# @app.router.lifecycle.on_shutdown()
# async def shutdown_event():
#     db.close()

# Define una ruta raíz con una operación get.
@app.get("/")
async def read_root():
    return {"message": "Bienvenido a mi API construida con FastAPI!"}
repository =  EntryRepository()
service = EntryService(repository)

@app.post("/entries/", response_model=EntryModel)
async def create_entry(entry_data: EntryModel):
    return service.create_entry(entry_data)

@app.get("/entries/", response_model=List[EntryModel])
async def get_entries():
    return service.get_entries()

@app.delete("/entries/{entry_id}")
async def delete_entry(entry_id: int):
    service.remove_entry(entry_id)
    return {"message": "Entry deleted"}