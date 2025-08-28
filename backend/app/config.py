from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # SQLite by default; swap to Postgres via env var in interviews that need it
    DATABASE_URL: str = "sqlite:///./dev.db"
    # during interviews keep it simple; Vite handles proxying so this is mostly for non-proxy runs
    CORS_ALLOW_ORIGINS: str = "*"  # comma-separated if you want specific origins

    class Config:
        env_file = ".env"

settings = Settings()
