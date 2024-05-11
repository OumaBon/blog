class Development:
    DEBUG = True
    SECRET_KEY = 'select_very_secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True