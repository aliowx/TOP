from pydantic import BaseModel, ConfigDict, EmailStr



class UserBase(BaseModel):
    email: EmailStr | None = None
    is_active: bool | None = True
    is_superuser: bool = False
    full_name: str | None = None



class UserCreate(UserBase):
    email: EmailStr
    password: str



class UserUpdate(UserBase):
    password: str | None = None


class UserInDBBase(UserBase):
    id: int | None = None
    model_config = ConfigDict(from_attributes=True)



class UserInDB(UserInDBBase):
    hashed_password: str


class UserIn(BaseModel):
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str
