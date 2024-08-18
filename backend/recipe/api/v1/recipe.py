from fastapi import APIRouter
from recipe.mock import recipes

from pydantic import BaseModel

class Recipe(BaseModel):
    id: int
    name: str
    ingredients: list[str]
    instructions: list[str]
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    tags: list[str]
    userId: int
    image: str
    mealType: list[str]

router = APIRouter()


@router.get("/recipes")
async def get_all_recipes():
    return {"recipes": recipes}

@router.get('/recipes/{id}')
async def get_recipes_by_id(id: int):
    filtered_recipe  = [recipe for recipe in recipes if recipe['id'] == id]
    return filtered_recipe

@router.post('/recipes')
async def post_recipe(recipe: Recipe):
    recipes.append(recipe.model_dump())
    return recipe

@router.put('/recipes/{id}')
async def put_recipe(id: int, recipe: Recipe):
    for i in recipes:
        if i['id'] == id:
            i['id'] = recipe
            return i['id']
    return {'msg':'recipe bulunamadi'}

@router.delete('/recipes/{id}')
async def delete_recipe(id: int):
    for i in recipes:
        if i['id'] == id:
            recipes.remove(i)
            return recipes
            
    return {'msg':'recipe bulunamadi'}
