from fastapi import APIRouter

router_v1 = APIRouter(prefix="/v1/users", tags=["users"])

@router_v1.get("/all-users")
async def get_users():
    return {"message": "Returning all users!"}
