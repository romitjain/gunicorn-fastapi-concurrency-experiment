APP_LOGGER_FORMAT = '["level": "%(levelname)s"] ["pid": "%(process)d", "thread_id": "%(thread)d"] ["endpoint": "{endpoint}", "path": {path}] "msg": "%(message)s"'
SERVER_LOGGER_FORMAT = '["level": "%(levelname)s"] ["pid": "%(process)d", "thread_id": "%(thread)d"] "msg": "%(message)s"'


logging_config = dict(
        version=1,
        disable_existing_loggers=False,
        root={
            "level": "INFO",
            "handlers": ["app1", "app2"]
        },
        formatters={
            "app": {
                "format": str(APP_LOGGER_FORMAT),
                "class": "logging.Formatter"
            },
            "server": {
                "format": str(SERVER_LOGGER_FORMAT),
                "class": "logging.Formatter"
            }
        },
        handlers={
            "app1": {
                "class": "logging.StreamHandler",
                "formatter": "app",
                "stream": "ext://sys.stdout"
            },
            "app2": {
                "class": "logging.StreamHandler",
                "formatter": "app",
                "stream": "ext://sys.stdout"
            },
            "server": {
                "class": "logging.StreamHandler",
                "formatter": "server",
                "stream": "ext://sys.stdout"
            }
        },
        loggers={
            "app1": {
                "level": "INFO",
                "handlers": ["app1"],
                "propagate": False,
            },
            "app2": {
                "level": "INFO",
                "handlers": ["app2"],
                "propagate": False,
            },
            "gunicorn.error": {
                "level": "INFO",
                "handlers": ["server"],
                "propagate": False,
            },
        },
)