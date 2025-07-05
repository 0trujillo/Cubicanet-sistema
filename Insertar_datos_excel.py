import pandas as pd
from sqlalchemy import create_engine

# 1. Cargar el Excel
df = pd.read_excel("trabajadores_prueba.xlsx")

# 2. Datos de conexión
usuario = "postgres"
contrasena = "Yojansel18"
host = "localhost"
puerto = "5432"
base_datos = "cubicanet"

# 3. Crear conexión con SQLAlchemy
engine = create_engine(f'postgresql+psycopg2://{usuario}:{contrasena}@{host}:{puerto}/{base_datos}')

# 4. Insertar los datos en la tabla correcta
df.to_sql('trabajador', engine, if_exists='append', index=False)

# 5. Verificar conexión
try:
    with engine.connect() as conn:
        print("✅ Conexión exitosa a la base de datos y datos insertados.")
except Exception as e:
    print("❌ Error al conectar:", e)
