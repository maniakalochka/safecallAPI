from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(..., title="Username", max_length=255)
    hashed_password: str = Field(..., title="Password", max_length=255)
    karma: int = Field(0, title="Karma", ge=0)


class SuperUserCreate(UserCreate):
    is_admin: bool = Field(True, title="Is Admin")


class UserRead(BaseModel):
    id: int = Field(..., title="User ID")
    username: str = Field(..., title="Username", max_length=255)
    karma: int = Field(0, title="Karma", ge=0) 

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """/TODO реализовать позже"""

    username: str = Field(None, title="Username", max_length=255)
    hashed_password: str = Field(None, title="Password", max_length=255)

    class Config:
        from_attributes = True


class KarmaUpdate(BaseModel):
    """/TODO реализовать карму позже"""
    karma: int = Field(..., title="Karma", ge=0)

    class Config:
        from_attributes = True  