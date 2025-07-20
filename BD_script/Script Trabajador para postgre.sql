-- 1) Limpiar esquema (orden de drops: vistas → tablas dependientes → tablas base)
DROP VIEW IF EXISTS asistencia_mensual;

DROP TABLE IF EXISTS asistencia_dia;
DROP TABLE IF EXISTS cuenta_deposito;
DROP TABLE IF EXISTS tipos_cuenta;
DROP TABLE IF EXISTS bancos;

DROP TABLE IF EXISTS contrato;
DROP TABLE IF EXISTS proyectos;
DROP TABLE IF EXISTS empleados;
DROP TABLE IF EXISTS estados_civil;
DROP TABLE IF EXISTS sistemas_salud;
DROP TABLE IF EXISTS afp;


-- 2) Tablas de catálogo básicas

CREATE TABLE afp (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE sistemas_salud (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE estados_civil (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(20) UNIQUE NOT NULL
);


-- 3) Catálogos para cuentas bancarias

CREATE TABLE bancos (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE tipos_cuenta (
  id     SERIAL PRIMARY KEY,
  nombre VARCHAR(50) UNIQUE NOT NULL
);


-- 4) Tabla de empleados (sin booleano de depósito)

CREATE TABLE empleados (
  id                SERIAL PRIMARY KEY,
  nombre            VARCHAR(120) NOT NULL,
  rut               VARCHAR(12) UNIQUE NOT NULL,
  correo_trabajador TEXT UNIQUE,
  fecha_nacimiento  DATE NOT NULL,
  estado_civil_id   INT REFERENCES estados_civil(id)
);


-- 5) Proyectos y contratos

CREATE TABLE proyectos (
  id            SERIAL PRIMARY KEY,
  nombre        VARCHAR(150) UNIQUE NOT NULL,
  fecha_inicio  DATE,
  fecha_termino DATE
);

CREATE TABLE contrato (
  id                SERIAL PRIMARY KEY,
  empleado_id       INT UNIQUE NOT NULL REFERENCES empleados(id),
  proyecto_id       INT NOT NULL REFERENCES proyectos(id),
  fecha_ingreso     DATE NOT NULL,
  afp_id            INT REFERENCES afp(id),
  sistema_salud_id  INT REFERENCES sistemas_salud(id),
  telefono_emp      VARCHAR(15),
  correo_empl       TEXT,
  sueldo_diario     NUMERIC(10,2),
  created_at        TIMESTAMPTZ DEFAULT now(),
  updated_at        TIMESTAMPTZ DEFAULT now()
);


-- 6) Asociación Empleado ↔ Cuenta de Depósito

CREATE TABLE cuenta_deposito (
  id             SERIAL PRIMARY KEY,
  empleado_id    INT NOT NULL UNIQUE REFERENCES empleados(id),
  banco_id       INT NOT NULL REFERENCES bancos(id),
  tipo_cuenta_id INT NOT NULL REFERENCES tipos_cuenta(id),
  numero_cuenta  VARCHAR(30) NOT NULL
);

