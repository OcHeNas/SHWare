from fastapi import FastAPI
from app.users.router import router_auth, router_users
from app.object.router import router_object
from app.object.components.router import router_components
from app.object.TW.router import router_TW
from app.object.work.router import router_Work
from app.object.components.manufacturer.router import router_manufacturer
from app.object.components.sensors.router import router_sensor
from app.object.components.sensors.values.router import router_values
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router_users)
app.include_router(router_auth)
app.include_router(router_object)
app.include_router(router_components)
app.include_router(router_TW)
app.include_router(router_Work)
app.include_router(router_manufacturer)
app.include_router(router_sensor)
app.include_router(router_values)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
