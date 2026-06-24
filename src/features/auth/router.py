from fastapi import APIRouter
from src.features.auth.schemas import LoginRequest, RegisterRequest
from fastapi.responses import JSONResponse

auth_router_v1 = APIRouter(prefix="/v1/auth", tags=["auth"])


@auth_router_v1.post("/login", tags=["auth"])
async def login(login_request: LoginRequest):
    print(f"Login request received: {login_request.email} {login_request.password}")
    return JSONResponse(content={"message": "Login successful!"}, status_code=200)




@auth_router_v1.post("/register", tags=["auth"])
async def register(registration_data: RegisterRequest):
    print(f"Register request received: {registration_data}")
    return JSONResponse(content={"message": "Register successful!"}, status_code=201)