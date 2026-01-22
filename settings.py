import sys
import os
from pathlib import Path

BASE_DIR = Path(getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = "this is a desktop app lol"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "data" / "db.sqlite3",
    }
}

INSTALLED_APPS = ("app.db",)
