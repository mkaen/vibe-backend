from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    phone: str
    email: str = Field(alias="email")
    password: str = Field(min_length=8)
    has_image: bool = Field(alias="hasImage", default=False)
