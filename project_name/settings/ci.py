from .dev import *

SECRET_KEY = "ci-secret-key-not-for-production"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test.db",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"