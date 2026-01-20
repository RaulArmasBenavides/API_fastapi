from datetime import datetime

from pydantic import BaseModel

from app.core.models.user import User

 

class SignIn(BaseModel):
    email__eq: str
    password: str


class SignUp(BaseModel):
    email: str
    password: str
    name: str


class Payload(BaseModel):
    id: int
    email: str
    name: str
    is_superuser: bool


class SignInResponse(BaseModel):
    access_token: str
    expiration: datetime
    user_info: User
