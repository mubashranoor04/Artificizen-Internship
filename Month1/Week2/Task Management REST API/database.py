from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database location
DATABASE_URL = "sqlite:///./tasks.db"

# Creates the connection (engine) to the database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
# Creates a new database session for every request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
# Base class for all database models
Base = declarative_base()