# test_db.py
import psycopg2

try:
    conn = psycopg2.connect(
        user="benjamin",
        password="Ben1258",
        host="192.168.100.149",
        port="5432",
        database="cubicanet"
    )
    print("✅ Conexión OK:", conn.status)
except Exception as e:
    print("❌ Error conectando:", e)
finally:
    if 'conn' in locals():
        conn.close()
