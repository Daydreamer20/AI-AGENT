from functools import lru_cache
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	app_name: str = "AI Trading Agent"
	environment: str = "development"
	debug: bool = True
	version: str = "0.1.0"

	# Database
	postgres_host: str = "localhost"
	postgres_port: int = 5432
	postgres_user: str = "postgres"
	postgres_password: str = "postgres"
	postgres_db: str = "trader"

	# Redis
	redis_host: str = "localhost"
	redis_port: int = 6379
	redis_db: int = 0

	# MCP endpoints
	context7_url: str = "http://localhost:8001"
	sequential_url: str = "http://localhost:8002"
	playwright_url: str = "http://localhost:8003"

	model_config = SettingsConfigDict(
		env_file=".env",
		env_file_encoding="utf-8",
		env_prefix="TRADER_",
	)

	@computed_field  # type: ignore[misc]
	@property
	def database_url(self) -> str:
		return (
			f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
			f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
		)

	def safe_dict(self) -> dict:
		return self.model_dump(exclude={"postgres_password"})


@lru_cache(maxsize=1)
def get_settings() -> Settings:
	return Settings()  # type: ignore[call-arg]