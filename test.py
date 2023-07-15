from pathlib import Path
import os
import environ

from todolist.settings import BASE_DIR
# Start Django-environ
env = environ.Env(
    DEBUG=(bool, False)
)
# reading .env file
env.read_env(os.path.join(BASE_DIR, '.env'))

print(env('PASSWORD_DB'))