# 🚀 Day 6 – Docker Compose

### 🔹 **What is Docker Compose?**

* Tool for defining & running multi-container apps.
* Uses a single **`docker-compose.yml`** file to describe all services (web app, db, cache, etc.).
* Instead of starting each container manually, you just do `docker-compose up`.

---

### 🔹 **Example: FastAPI + Postgres**

`docker-compose.yml`

```yaml
version: "3"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

👉 Breakdown:

* **`web`** → builds your FastAPI app (from `Dockerfile`).
* **`db`** → uses official Postgres image.
* **`environment`** → sets username, password, db name.
* **`volumes`** → ensures DB data persists even if container restarts.

---

### 🔹 **Commands**

1. **Start services (detached mode)**

```bash
docker-compose up -d
```

2. **Check running containers**

```bash
docker-compose ps
```

3. **Stop all services**

```bash
docker-compose down
```

4. **View logs (live)**

```bash
docker-compose logs -f
```

---

### 📝 Day 6 Task

1. Add the above `docker-compose.yml` in your FastAPI project.
2. Run `docker-compose up -d`.
3. Verify:

   * FastAPI app runs at 👉 `http://localhost:8000`
   * Postgres is running (use `docker ps`).
4. Try stopping with `docker-compose down`.

---

