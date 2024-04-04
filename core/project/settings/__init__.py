from split_settings.tools import optional, include
import os
from pathlib import Path

# Decouple
from decouple import Csv, config
from dotmap import DotMap
# from split_settings.tools import include

# init environment variables
ENV = DotMap({'config': config, 'csv': Csv})

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Build paths inside the project directory
# PROJECT_DIR = os.path.join(BASE_DIR, 'core/project')

# Admin path
ADMIN_PATH = ENV.config('ADMIN_PATH')

# Debug
DEBUG = ENV.config('DEBUG', cast = bool)


include(
    'base.py',
    'utils_config.py',
)

if DEBUG:
    include('development.py')
else:
    include('production.py')

# # Include the base settings file
# include(
#     'base.py',
#     'utils_config.py',
#     'general_security.py',
#     'admin_template_config.py',
# )

# # Include the environment-specific settings file based on the environment
# if config('DJANGO_ENV') == 'Development':
#     include('development.py')
# elif config('DJANGO_ENV') == 'Production':
#     include('production.py')
