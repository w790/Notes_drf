from pathlib import Path
from decouple import config

#Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent
#Секретный ключ для безопасности,объязательно хранить в .env
SECRET_KEY = config('SECRET_KEY')
#Режим отладки
DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS',default='').split(',')


#Список встроенных джанго приложений
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#Список сторонних приложений
THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
]

#Список локальных приложений
LOCAL_APPS = [
    'apps.notes',
]
#Общий список
INSTALLED_APPS=DJANGO_APPS+THIRD_PARTY_APPS+LOCAL_APPS

#Список MIDDLEWARE для обработки запросов
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#Корневой url файл проекта
ROOT_URLCONF = 'notes_project.urls'
#Конфигурация шаблонов джанго
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'notes_project.wsgi.application'


#Конфигурация БД
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': '5432',
    }
}


#Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#Настройка интернациональности,Язык в админке
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


#Статические файлы
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Настройки Django REST Framework
REST_FRAMEWORK = {
    #Классы разрешений
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny', #Разрешить доступ всем
    ],

    #Классы ограничения запросов
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle', # Ограничение для анонимных пользователей
    ],

    #Лимиты запросов
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour', # 100 запросов в час для анонимных пользователей
    },

    #Классы рендеринга
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer', # Рендеринг в JSON
    ],

    #Классы парсинга
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser', # Парсинг JSON-данных
    ],
}
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True  # Для разработки
else:# Для продакшена
    CORS_ALLOWED_ORIGINS = [
        "https://localhost:5173",
        "https://127.0.0.1:5173",
    ]
#Настройки безопасности
SECURE_BROWSER_XSS_FILTER = True #Защита от XSS-атак
SECURE_CONTENT_TYPE_NOSNIFF = True #Запрет MIME-типов
X_FRAME_OPTIONS = 'DENY' #Защита от кликджекинга

# Настройки логирования
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log', #Лучше хранить логи в отдельной папке
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}