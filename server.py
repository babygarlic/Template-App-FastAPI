from app.core.config import settings
import uvicorn
from main import app

if __name__=="__main__":
    uvicorn.run("server:app", host=settings.HOST, port=settings.PORT, reload=True)