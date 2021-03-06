import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from app.database.database import engine, get_db
from app.routers.auth.auth import oauth2_scheme
from app.routers.lights import lights
from app.routers.lights import models as light_models
from app.routers.machines import machines
from app.routers.machines import models as machines_models
from app.routers.auth import auth
from app.routers.auth import models as auth_models
from app.settings import app_title, app_version, tags_metadata, app_description

load_dotenv()

machines_models.Base.metadata.create_all(bind=engine)
light_models.Base.metadata.create_all(bind=engine)
auth_models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=app_title,
    description=app_description,
    version=app_version,
    openapi_tags=tags_metadata
)

app.include_router(
    machines.router,
    prefix="/machines",
    dependencies=[Depends(oauth2_scheme)],
    tags=["machines"]
)

app.include_router(
    lights.router,
    prefix="/lights",
    dependencies=[Depends(oauth2_scheme)],
    tags=["lights"]
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"]
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
