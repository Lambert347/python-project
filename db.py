import psycopg2 

con = psycopg2.connect(
    host = "localhost",
    database = "demo_db",
    user = "ianlambert",
    password = "postgres",
    port = 5432
)

cur = con.cursor()

cur.execute("select id, name from employees")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name {r[1]}")
   
cur.close()


con.close()