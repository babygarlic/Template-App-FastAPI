from fastapi import FastAPI
from fastapi import Request, Response
from app.api import task, user
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

@app.get("/")
def read_root():
    return {"Hello": "World"}
