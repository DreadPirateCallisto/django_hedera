from core.project.settings import BASE_DIR, ENV
from core.project.settings import ENV, DEBUG

# Secrete key
SECRET_KEY = ENV.config('SECRET_KEY')

# Allowed Host
ALLOWED_HOSTS = ENV.config('ALLOWED_HOSTS', default='127.0.0.1', cast=ENV.csv())

# Debug
DEBUG = DEBUG

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # Security Settings
# X_FRAME_OPTIONS = 'DENY'
