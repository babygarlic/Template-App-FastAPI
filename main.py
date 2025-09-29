from fastapi import FastAPI
from app.api import task, user, auth
from app.core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=[""],  # Adjust this to your frontend's URL in production
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )

Base.metadata.create_all(bind=engine)

app.include_router(task.router,prefix='/task')
app.include_router(user.router,prefix='/user')
app.include_router(auth.router,prefix='/auth')

@app.get("/")
def read_root():
    return {"Hello": "World"}
