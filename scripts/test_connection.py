import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect(
        dbname="datamart",
        user="neondb_owner",
        password="npg_2MoHYqITnC5F",
        host="ep-dawn-frost-a598gzm4-pooler.us-east-2.aws.neon.tech",
        port="5432",
        sslmode="require"  # Pastikan SSL diaktifkan
    )
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM public."datamart" LIMIT 5;')
    rows = cursor.fetchall()
    print("Data preview:")
    for row in rows:
        print(row)
    conn.close()

except Exception as e:
    print("Connection failed:", e)
