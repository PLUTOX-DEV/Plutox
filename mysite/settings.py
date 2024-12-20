"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$=&wb-z6541xc(f%$y2lek_1x@e(&jm3&w=!xv@+2=&wqzygsl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['plutox.onrender.com']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'viewflow',
    'base',
    'rest_framework',
    "corsheaders",
]
AUTH_USER_MODEL = 'base.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = (BASE_DIR/'staticfiles')
STATICFILES_DIRS = [
    BASE_DIR/'static'
]

MEDIA_URL = '/images/'


MEDIA_ROOT = BASE_DIR / 'static/images'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


JAZZMIN_SETTINGS = {
    # Title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Chat Admin",

    # Title on the login screen (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Chatting Admin",

    # Title on the brand (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "ChatApp",

    # Logo to use for your site, must be present in static files, used for the brand in the top left
    "site_logo": "images/chat_login_logo.png",

    # Logo to use on the login screen (defaults to site_logo)
    "login_logo": "images/chat_login_logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Plutox Admin Panel",

    # Copyright text in the footer
    "copyright": "PlutoxApp © 2024",

    # Search bar options: specify the models to include in search results
    "search_model": ["auth.User", "base.Topic", ],

    # Field name on the user model that contains avatar ImageField/URLField/Charfield
    "user_avatar": "profile_picture",  # Use your user model's avatar field name

    # Sidebar settings
    "show_sidebar": True,  # Display the sidebar
    "navigation_expanded": True,  # Automatically expand the menu
    "hide_apps": ["sessions"],  # Apps to hide from the menu
    "hide_models": [],  # Models to hide from the menu

    # Order of apps and models in the side menu
    "order_with_respect_to": [
        "auth",  # User and Group management
        "chat",  # Chat-related models
        "chat.ChatRoom",
        "chat.Message",
    ],

    "custom_links": {
        "chat": [
            {
                "name": "Create Chat Room",
                "url": "admin:chat_chatroom_add",
                "icon": "fas fa-comments",
                "permissions": ["chat.add_chatroom"],
            },
            {
                "name": "Send Broadcast",
                "url": "broadcast_message",  # Correctly named Django URL
                "icon": "fas fa-bullhorn",
                "permissions": ["chat.add_message"],
            },
        ],
    },

    # Icons for models/apps
    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "chat.ChatRoom": "fas fa-comments",
        "chat.Message": "fas fa-envelope",
    },

    # Themes and UI
    "changeform_format": "horizontal_tabs",  # Use tabs in the admin form
    "changeform_format_overrides": {
        "auth.user": "collapsible",  # Example for specific models
    },
    "show_ui_builder": True,  # Show Jazzmin's UI builder for admin customization
}


CORS_ALLOW_ALL_ORIGINS = True
