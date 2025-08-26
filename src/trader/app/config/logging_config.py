from logging.config import dictConfig


def configure_logging(level: str = "INFO") -> None:
	dictConfig(
		{
			"version": 1,
			"disable_existing_loggers": False,
			"formatters": {
				"default": {
					"format": "%(asctime)s %(levelname)s %(name)s - %(message)s",
					"datefmt": "%Y-%m-%d %H:%M:%S",
				}
			},
			"handlers": {
				"console": {
					"class": "logging.StreamHandler",
					"formatter": "default",
				}
			},
			"root": {"level": level, "handlers": ["console"]},
		}
	)