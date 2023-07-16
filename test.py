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

print(env('POSTGRES_PASSWORD'))
print(env('POSTGRES_USER'))
print(env('POSTGRES_DB'))