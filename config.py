from dotenv import load_dotenv
import os

class Config:
    def __init__(self, env_path: str):
        """Initialize and load the .env file from the given path."""
        load_dotenv(dotenv_path=env_path)
    
    def get(self, key: str, default=None):
        """Get the environment variable value for the given key, or return the default value."""
        return os.getenv(key, default)
