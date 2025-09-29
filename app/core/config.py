from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI App Template"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    HOST: str=os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT_SERVER",8000))
    SENDER_EMAIL: str = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD: str = os.getenv("SENDER_PASSWORD")
    EXPRIES_DELTA: int = int(os.getenv("EXPRIES_DELTA", 3600))
    TOKEN_TYPE: str = os.getenv("TOKEN_TYPE", "Bearer")     

settings = Settings()