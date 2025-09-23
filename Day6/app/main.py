from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Hello from FastAPI + Docker Compose 🚀"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            dbname="mydb",
            user="user",
            password="pass",
            host="db",   # 👈 service name from docker-compose
            port=5432
        )
        conn.close()
        return {"db_status": "Connected ✅"}
    except Exception as e:
        return {"db_status": "Error ❌", "details": str(e)}
