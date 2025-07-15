import pandas as pd
from sqlalchemy import create_engine

# 1. Cargar el Excel
df = pd.read_excel(".xlsx")  # Aqui podemos cambiar el nombre de nuestro excel antes del punto

# 2. Conexión a PostgreSQL (es obvio lo que hay que poner)
usuario = "tu_usuario"
contrasena = "tu_contraseña"
host = "localhost"
puerto = "5432"
base_datos = "nombre_basedatos"

# 3. Crear la conexión usando SQLAlchemy (lo mismo de arriba)
engine = create_engine(f'postgresql+psycopg2://{usuario}:{contrasena}@{host}:{puerto}/{base_datos}')

# 4. Insertar los datos en la tabla (' ' aqui tenemos que poner el nombre de la tabla)
df.to_sql('', engine, if_exists='append', index=False)