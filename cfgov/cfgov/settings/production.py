from .base import *

# Sends an email to developers in the ADMIN_EMAILS list if Debug=False for errors
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')

if os.environ.get('DATABASE_ROUTING', False):
    DATABASE_ROUTERS = ['v1.db_router.CFGOVRouter', 'v1.db_router.LegacyRouter']

    DATABASES = {
        'default': {
            'ENGINE': MYSQL_ENGINE,
            'NAME': os.environ.get('MYSQL_NAME', ''),
            'USER': os.environ.get('MYSQL_USER', ''),
            'PASSWORD': os.environ.get('MYSQL_PW', ''),
            'HOST': os.environ.get('MYSQL_HOST', ''),
            'PORT': os.environ.get('MYSQL_PORT', ''),
        },
        'legacy': {
            'ENGINE': MYSQL_ENGINE,
            'NAME': os.environ.get('LEGACY_MYSQL_NAME', ''),
            'USER': os.environ.get('LEGACY_MYSQL_USER', ''),
            'PASSWORD': os.environ.get('LEGACY_MYSQL_PW', ''),
            'HOST': os.environ.get('LEGACY_MYSQL_HOST', ''),
            'PORT': os.environ.get('LEGACY_MYSQL_PORT', ''),
        },
    }
