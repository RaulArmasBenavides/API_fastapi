# Importa FastAPI
from typing import List

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.v1.routes import routers as v1_routers
from app.core.container import Container
from app.util.class_object import singleton
from app.core.models.config import configs
 
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

 
@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=configs.PROJECT_NAME,
            openapi_url=f"{configs.API}/openapi.json",
            version="0.0.1",
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()
        # self.db.create_database()

        # set cors
        if configs.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in configs.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(v1_routers, prefix=configs.API_V1_STR)
        # self.app.include_router(v2_routers, prefix=configs.API_V2_STR)


app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container