from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine(
    "sqlite:///canculator.db",
    echo=True,
)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    ...

def create_db():
    Base.methadata.create_all(blind=engine)

def drop_db():
    Base.methadata.drop_all(blind=engine)