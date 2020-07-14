import os

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SECRET_KEY = '6$n49vdmi8i(!3%$gg@zc5qbj4b*92q+7tz#5(u^m1dhns193p'

DEBUG = False

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DATABASES = {
    'default': dj_database_url.config()
}
