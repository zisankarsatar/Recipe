from fastapi import FastAPI, APIRouter
from recipe.api.router import v1router


app = FastAPI()
router = APIRouter()

@router.get("/")
async def main():
    return {"msg": "Hello Canim"}

@router.get('/health')
async def health_check():
    return {'status': 'healthy'}


app.include_router(router)
app.include_router(v1router)