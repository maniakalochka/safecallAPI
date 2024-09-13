from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.user import User

from src.schemas.user_schemas import UserCreate, SuperUserCreate


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    user_data = user.model_dump()
    user = User(**user_data)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user 


async def create_superuser(db: AsyncSession, user: SuperUserCreate) -> User:
    user_data = user.model_dump()
    super_user = User(**user_data)
    db.add(super_user)
    await db.commit()
    await db.refresh(super_user)
    return super_user



async def get_user(db: AsyncSession,
                   skip: int  = 0,
                   limit: int = 100) -> User:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

