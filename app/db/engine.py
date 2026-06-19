from sqlalchemy import create_engine
from config.settings import settings

if not settings.DATABASE_URL:
    raise Exception("DATABASE_URL is not configured")

engine = create_engine(settings.DATABASE_URL)