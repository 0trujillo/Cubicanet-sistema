Cubicanet-sistema

Insertar datos de Excel a PostgreSQL
Dependencias necesarias
Para manejar la lectura de archivos Excel y la conexión a la base de datos PostgreSQL, necesitas instalar las siguientes librerías de Python:

pandas: para leer y manipular archivos Excel.

openpyxl: motor para que pandas pueda leer archivos .xlsx.

sqlalchemy: para gestionar la conexión a PostgreSQL.

psycopg2-binary: adaptador PostgreSQL para Python.

Comando para instalar las dependencias necesarias: pip install pandas openpyxl sqlalchemy psycopg2-binary

Características:
-  Importación masiva de datos desde archivos Excel (.xlsx) a PostgreSQL.
-  Validación básica de datos antes de insertar.
-  Generación de registro de errores para filas con formatos inválidos.
-  Visualización dinámica de la "pseudo-tabla" usando Tabulator en un frontend con Vue.js
-  Enlaces dinámicos (hypervínculos) para navegación entre registros.
