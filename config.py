import secrets


class Config:
    SECRET_KEY = secrets.token_hex(24)
    DEBUG = True
