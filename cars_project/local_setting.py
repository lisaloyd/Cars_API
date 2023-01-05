# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x=du10899gk%le_fogwm*8s@9*ceaqv=d*8k981sv)bd-3d@^-'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}