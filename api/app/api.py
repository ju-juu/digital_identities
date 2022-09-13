from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import sign_jwt
from app.data.handler import check_user, write_user, get_user
from app.data.model import UserSchema, UserLoginSchema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return 'welcome to QRID'


@app.post("/validate_token", dependencies=[Depends(JWTBearer())])
async def add_post(user: UserLoginSchema) -> dict:
    if check_user(user):
        return {
            "data": "Token Valid"
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )


@app.post("/user/signup")
async def create_user(user: UserSchema = Body(...)):
    if not get_user(user.email):
        write_user(user)
        return sign_jwt(user.email)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="A user with this email already exists.",
        )


@app.post("/user/login")
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return sign_jwt(user.email)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Login details are incorrect.",
        )
