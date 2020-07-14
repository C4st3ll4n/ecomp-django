from .settings import *
import dj_database_url

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEBUG = True

MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DATABASES = {
    'default': dj_database_url.config()
}
