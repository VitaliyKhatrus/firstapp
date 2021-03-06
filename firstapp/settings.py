"""
Django settings for firstapp project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$opv2dc34_c_wr(^&mij79(*u^mldmrk!uy(6a_@i1ynoiuw0@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True ### On production server must be False!!!

ALLOWED_HOSTS = []

# TEMPLATE_DIRS = (
#     '/home/solid/djangoenv/bin/firstapp/templates',
#     '/home/solid/djangoenv/bin/firstapp/article/templates',
#     '/home/solid/djangoenv/bin/firstapp/loginsys/templates',
# )

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'article',
    'loginsys',
    'disqus',
)

DISQUS_API_KEY = 'RUx7Awd5TNn5ysXf4u82XQns03oYoSBNqRKhaDtDLVCHRRJOjDkUcvGMVrrIeHNu'
DISQUS_WEBSITE_SHORTNAME = 'blog-cvflpgdpdw'

GRAPPELLI_ADMIN_TITLE = 'My BLOG'

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

ROOT_URLCONF = 'firstapp.urls'

##TEMPLATES = [
##    {
##        'BACKEND': 'django.template.backends.django.DjangoTemplates',
##        'DIRS': [],
##        'APP_DIRS': True,
##        'OPTIONS': {
##            'context_processors': [
##                'django.template.context_processors.debug',
##                'django.template.context_processors.request',
##                'django.contrib.auth.context_processors.auth',
##                'django.contrib.messages.context_processors.messages',
##            ],
##        },
##    },
##]

WSGI_APPLICATION = 'firstapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'our_db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
      os.path.join(PROJECT_ROOT, 'assets'),
      )
#STATICFILES_DIRS = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
#MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

# STATICFILES_DIRS = (
#    ('static', '/home/solid/django_blog/firstapp/assets'),
# )
#CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
#CKEDITOR_JQUERY_URL = 'http://libs.baidu.com/jquery/2.0.3/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"
#CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True

CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'removePlugins': 'stylesheetparser',
        'toolbar': 'Full',
        'height': 500,
        'width': 900,
    },
}
#CKEDITOR_UPLOAD_PATH = '/home/solid/django_blog/firstapp/media/uploads/'
CKEDITOR_UPLOAD_PATH = ''
# STATICFILES_FINDERS = (
# 'django.contrib.staticfiles.finders.FileSystemFinder',
# 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )


#AUTH_USER_MODEL = 'auth.User'
print CKEDITOR_UPLOAD_PATH
print MEDIA_ROOT
