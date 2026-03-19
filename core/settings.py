from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / 'db.sqlite3'

class Db_Config(BaseModel):
    """Настройки базы данных"""
    url: str = f'sqlite+aiosqlite:///{DB_PATH}'


class CORS_Config(BaseModel):
    """Настройки CORS"""
    allow_credentials: bool = True
    allow_origins: list[str] = ['*']
    allow_methods: list[str] = ['*']
    allow_headers: list[str] = ['*']


class App_Config(BaseModel):
    """Настройки приложения"""
    debug: bool = False
    host: str = '0.0.0.0'
    port: int = 8000
    reload: bool = True

class Settings(BaseSettings):
    """Базовые настройки"""
    app: App_Config = App_Config()
    cors: CORS_Config = CORS_Config()
    db: Db_Config = Db_Config()
    
    model_config = SettingsConfigDict(
        env_file = BASE_DIR / '.env',
        env_file_encoding = 'utf-8',
        case_sensitive = False,
        env_nested_delimiter='__',
        extra='ignore',
    )

settings = Settings()