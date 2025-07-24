# backend/db/connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Datos de conexión
DB_USER = "benjamin"
DB_PASSWORD = "Ben1258"
DB_HOST = "192.168.100.149"
DB_PORT = 5432
DB_NAME = "cubicanet"   # ajusta si tu base se llama distinto

# URI de SQLAlchemy
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Engine y sesión
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Dependency para FastAPI o función de helper en Flask:
    yield una sesión y ciérrala luego.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
