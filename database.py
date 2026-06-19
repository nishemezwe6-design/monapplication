from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://app_dqn4_user:qnxY2gROlrFdUxhxFUm1Vtl4qnpOXbuB@dpg-d8qf2khkh4rs73cbim50-a.oregon-postgres.render.com/app_dqn4"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()