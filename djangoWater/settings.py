# coding: utf-8
import os

PROJECT_NAME = 'Water battle'
PROJECT_DESC = 'Nullam viverra odio dui ornare suspendisse' \
               ' nam est conubia quisque phasellus in tristique penatibus neque' \
               ' faucibus fringilla aliquam himenaeos elit enim'
PROJECT_TIME = '7:30 - 17:30'
PROJECT_PHONE = '+7-906-198-3198'
PROJECT_PLACE = 'Water Wars.'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '$&y%-rjmg7@5be7jhv&4qpkg*&s4@0hlz96&*4^+yqaxbky)og'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'users.User'
INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'users',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
ROOT_URLCONF = 'djangoWater.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.site_meta',
            ],
        },
    },
]
WSGI_APPLICATION = 'djangoWater.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Asia/Novosibirsk'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)
STATICFILE_DIRS = (
    os.path.join(BASE_DIR, 'core/static')
)
STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/files/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'files')
LOGIN_REDIRECT_URL = '/'
LOGIN_AFTER_SIGNUP = True
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
# SESSION_ENGINE = 'redis_sessions.session'
# CACHE = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCach',
#         'LOCATION': '/var/run/redis/redis.sock',
#     }
# }
