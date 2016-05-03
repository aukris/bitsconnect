DEBUG = False
#SECURE_SSL_REDIRECT = True
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DATABASES = DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bitsconnect$default',
        'USER': 'bitsconnect',
        'PASSWORD': 'namburi1234',
        'HOST': 'bitsconnect.mysql.pythonanywhere-services.com',
    }
}
