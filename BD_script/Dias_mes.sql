-- Suponiendo que tienes una tabla empleados(id, nombre)

-- Genera una tabla de días del 1 al 31
WITH dias AS (
    SELECT generate_series(1, 31) AS dia
),
fechas AS (
    SELECT
        e.id AS empleado_id,
        e.nombre,
        y.año,
        m.mes,
        d.dia,
        make_date(y.año, m.mes, d.dia) AS fecha
    FROM empleados e
    CROSS JOIN (SELECT DISTINCT EXTRACT(YEAR FROM fecha)::INT AS año FROM asistencia_dia) y
    CROSS JOIN (SELECT DISTINCT EXTRACT(MONTH FROM fecha)::INT AS mes FROM asistencia_dia) m
    CROSS JOIN dias d
    WHERE make_date(y.año, m.mes, d.dia) <= make_date(y.año, m.mes, 
        EXTRACT(DAY FROM (date_trunc('month', make_date(y.año, m.mes, 1)) + INTERVAL '1 month - 1 day')))
)
SELECT
    f.empleado_id,
    f.nombre,
    f.año,
    f.mes,
    JSON_OBJECT_AGG(
        f.dia::TEXT,
        COALESCE(a.estado, 'F')  -- Aquí puedes cambiar 'F' por 'L' o 'P' según lo que prefieras mostrar por defecto
        ORDER BY f.dia
    ) AS dias
FROM fechas f
LEFT JOIN asistencia_dia a
    ON a.empleado_id = f.empleado_id
    AND a.fecha = f.fecha
GROUP BY f.empleado_id, f.nombre, f.año, f.mes;
