from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import robot, user, address, distribution

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(robot.router, prefix="/api")
app.include_router(user.router, prefix="/api")
app.include_router(address.router, prefix="/api")
app.include_router(distribution.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the RSH"}
