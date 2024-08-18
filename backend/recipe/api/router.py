from fastapi import APIRouter
from .v1.recipe import router as recipe_router


v1router = APIRouter(prefix="/api/v1", tags=["v1"])
v1router.include_router(recipe_router)
