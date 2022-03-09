import os
CONF = {
'version': 1,
'disable_existing_loggers': False,
'formatters': {
    'default': {
        "()": "uvicorn.logging.DefaultFormatter",
        "format": "%(levelprefix)s %(asctime)s | %(message)s",
        'datefmt': '%Y-%m-%d %H:%M:%S'
    },
},
'handlers': {
    'console': {
        'level': os.environ.get('LOG_LEVEL', 'DEBUG'),
        'formatter': 'default',
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout'
    },
    'file': {
        'level': os.environ.get('LOG_LEVEL', 'DEBUG'),
        'formatter': 'default',
        'class': 'logging.handlers.TimedRotatingFileHandler',
        'filename': 'fast_api_test.log',
    },
},
'loggers': {
    '': {
        'handlers': ['console', 'file'],
        'level': os.environ.get('LOG_LEVEL', 'DEBUG'),
        'propagate': False
    }
}
}