from pydantic_settings import BaseSettings
 
 
class Settings(BaseSettings):
 
    PROJECT_NAME: str = "Multi Tenant SaaS Backend"
    API_VERSION: str = "v1"
 
    DATABASE_URL: str = "sqlite:///./test.db"
 
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
 
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
 
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
 
    model_config = {"env_file": ".env"}
 
 
settings = Settings()
