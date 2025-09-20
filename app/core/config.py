from dotenv import load_dotenv
import os

load_dotenv()  # Đọc file .env

class Settings:
    PROJECT_NAME: str = "FastAPI App Template"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    #SECRET_KEY: str = os.getenv("SECRET_KEY")
    #DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    HOST: str=os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT_SERVER",8000))

settings = Settings()