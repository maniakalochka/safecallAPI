from fastapi import APIRouter, Depends, HTTPException
from src.db.db_config import get_db
from src.schemas.user_schemas import UserCreate, SuperUserCreate
from src.service.service_user import create_user, create_superuser

router = APIRouter()

@router.post("/sign-up/", response_model=UserCreate)
async def create_user_endpoint(user: UserCreate, db = Depends(get_db)):
    return await create_user(db, user)

@router.post("/sign-up/super/", response_model=SuperUserCreate)
async def create_super_user_endpoint(user: SuperUserCreate, db = Depends(get_db)):
    return await create_superuser(db, user)






