from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# حفاظت کے لیے، اصل یوزرنیم اور پاسورڈ کو Deployment سے پہلے ہٹائیں یا Environment Variables میں استعمال کریں
EMAIL_HOST_USER = 'hasnan05110@gmail.com' 
EMAIL_HOST_PASSWORD = 'mcea unre odiz iqim'    
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-^**5z+89d1o3kjcvt0dmtocfwi05)kg4-6^@#s*-mym9cx$^t1'

# VERCEL DEPLOYMENT KE LIYE ZARURI TABDEELIYAN:

# 1. DEBUG ko False karen
DEBUG = False

# 2. ALLOWED_HOSTS mein Vercel domain shamil karen
ALLOWED_HOSTS = [
    '.vercel.app',  # Vercel ke subdomains ke liye
    'e-commerce-seven-beta-19.vercel.app', # Aapka khaas domain
    '127.0.0.1', 
    'localhost',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
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

WSGI_APPLICATION = 'ecommerce_site.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation... (baqi sub wahi rahega)

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


# Internationalization... (wahi rahega)

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# STATIC FILES KE LIYE ZARURI TABDEELIYAN:

# 3. STATIC_URL ko sirf ek bar rakhen aur STATIC_ROOT shamil karen
import os
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Vercel/Production ke liye lazmi: Static files ko jama karne ki jagah
STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA FILES
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')