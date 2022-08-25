from pydantic import BaseSettings


class Settings(BaseSettings):
    mac = 'my mac address'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
