
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'dummy-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'charts',
]

MIDDLEWARE = []

ROOT_URLCONF = 'stock_chart_project.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'charts', 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {},
}]

WSGI_APPLICATION = 'stock_chart_project.wsgi.application'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'charts', 'static')]
