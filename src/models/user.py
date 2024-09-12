from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean,select
from sqlalchemy.orm import relationship

from src.db.db_config import get_db
from src.db.db_config import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    karma = Column(Integer, default=0)

async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield session