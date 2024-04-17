from fastapi import APIRouter

from app.api.v1.endpoints.entries import router as entries_router
 
routers = APIRouter()
router_list = [entries_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
