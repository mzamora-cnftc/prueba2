from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///facturacion.db"  # Cambiar a la URL de MariaDB si es necesario

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))  # <-- Cambiado a 'Session'
Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()