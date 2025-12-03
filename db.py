import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Render will supply this as an environment variable
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    # This will show up in the logs if we forget to set it
    raise RuntimeError("DATABASE_URL is not set")

# Create a connection pool to Postgres
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
