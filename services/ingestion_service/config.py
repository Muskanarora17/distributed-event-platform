from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.development",
        extra="ignore",
    )

    app_name: str
    app_version: str
    environment: str


settings = Settings()