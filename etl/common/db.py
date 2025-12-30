import psycopg2

from .config import get_db_config, load_env

load_env()
print(get_db_config())