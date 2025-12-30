# etl/common/config.py
import os

def load_env(env_file: str = ".env") -> None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except Exception:
        pass

def get_env(key, default=None, required=True):
    val = os.getenv(key, default)
    if required and (val is None or val == ""):
        raise RuntimeError(f"Missing required environment variable {key}")
    
    return val

def get_db_config() -> dict[str, str]:
   cfg = {
        "host": get_env("POSTGRES_HOSTNAME", required=True),
        "port": get_env("POSTGRES_PORT", "5432"),
        "dbname": get_env("POSTGRES_DBNAME", "5432"),
        "user": get_env("POSTGRES_USER", required=True),
        "password": get_env("POSTGRES_PASSWORD", "5432"),
        "schema": get_env("POSTGRES_SCHEMA", "5432")
    }
   
   return cfg