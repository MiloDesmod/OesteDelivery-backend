# core/settings.py
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-nva1fs!9$@m11!263g9i(_epm*ruh$rlwh$lense^g^cgie!@c'
DEBUG = True
ALLOWED_HOSTS = ['10.10.1.10', '10.10.1.15', '127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'locales',
    'ordenes',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates','DIRS': [],'APP_DIRS': True,'OPTIONS': {'context_processors': ['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages',],},},]
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': BASE_DIR / 'db.sqlite3',}}
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------------------------------------------------------------
# --- CONFIGURACIÓN DE AUTENTICACIÓN FINAL ---
# -----------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTH_USER_MODEL = 'usuarios.Usuario'
SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

# --- CONFIGURACIÓN CORRECTA Y UNIFICADA ---
# Se usa REST_AUTH, no REST_AUTH_SERIALIZERS
REST_AUTH = {
    'USER_DETAILS_SERIALIZER': 'usuarios.serializers.UsuarioSerializer',
    #'REGISTER_SERIALIZER': 'usuarios.serializers.CustomRegisterSerializer',
}

# Configuración de django-allauth
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# Le decimos a allauth que el registro está manejado por nuestro serializer personalizado
ACCOUNT_ADAPTER = 'allauth.account.adapter.DefaultAccountAdapter'