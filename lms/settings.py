"""
Django settings for lms project.
"""

from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING
SECRET_KEY = 'django-insecure-lt50uz-q0-_acce01r4glloiin@bk@g4jdn8(^j+7)sqk9@zyv'

DEBUG = True


# ✅ IMPORTANT FIX (CSRF + LOCALHOST)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# =====================================================
# APPLICATIONS
# =====================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps
    'accounts',
    'core',
    'courses',
    'student',
    'teacher',
    'adminpanel',
]


# =====================================================
# MIDDLEWARE
# =====================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    # ✅ CSRF Middleware MUST Stay Enabled
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'lms.urls'


# =====================================================
# TEMPLATES
# =====================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # ✅ Global Templates Folder
        'DIRS': [BASE_DIR / "templates"],

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


WSGI_APPLICATION = 'lms.wsgi.application'


# =====================================================
# DATABASE
# =====================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lms',
        'USER': 'lmsuser',
        'PASSWORD': 'lms',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# =====================================================
# PASSWORD VALIDATION
# =====================================================
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


# =====================================================
# LANGUAGE & TIMEZONE
# =====================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True


# =====================================================
# STATIC FILES
# =====================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]


# =====================================================
# LOGIN / LOGOUT SETTINGS ✅ FIXED
# =====================================================
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

# ✅ LOGOUT FIX: Redirect to Home Page after logout
LOGOUT_REDIRECT_URL = "/"


# =====================================================
# DEFAULT PRIMARY KEY
# =====================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
