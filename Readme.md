# 🚀 Docker 7-Day Roadmap

### **Day 1 – Setup & First Container**

* Install Docker Desktop (Windows/Mac) ya Docker Engine (Linux).
* Verify installation:

  ```bash
  docker --version
  docker run hello-world
  ```
* Explore running containers:

  ```bash
  docker ps
  docker ps -a
  ```
* Stop / Start container:

  ```bash
  docker stop <id>
  docker start <id>
  ```

---

### **Day 2 – Images**

* Pull images:

  ```bash
  docker pull ubuntu
  docker pull python:3.10
  ```
* List & remove images:

  ```bash
  docker images
  docker rmi <id>
  ```
* Run Python in container:

  ```bash
  docker run -it python:3.10 python
  ```

---

### **Day 3 – Container Lifecycle**

* Interactive container:

  ```bash
  docker run -it ubuntu bash
  ```
* Exec into running container:

  ```bash
  docker exec -it <id> bash
  ```
* Remove container:

  ```bash
  docker rm <id>
  ```

---

### **Day 4 – Dockerfile**

* Create `Dockerfile`:

  ```dockerfile
  FROM python:3.10
  WORKDIR /app
  COPY . .
  CMD ["python", "app.py"]
  ```
* Build & run:

  ```bash
  docker build -t myapp .
  docker run myapp
  ```

---

### **Day 5 – Ports & Volumes**

* Port mapping:

  ```bash
  docker run -p 8000:8000 myapp
  ```
* Mount volumes:

  ```bash
  docker run -v $(pwd):/app myapp
  ```

---

### **Day 6 – Docker Compose**

* Create `docker-compose.yml`:

  ```yaml
  version: "3"
  services:
    web:
      build: .
      ports:
        - "8000:8000"
    db:
      image: postgres:15
      environment:
        POSTGRES_USER: user
        POSTGRES_PASSWORD: pass
  ```
* Run services:

  ```bash
  docker-compose up -d
  docker-compose down
  ```

---

### **Day 7 – Mini Project**

* FastAPI + PostgreSQL app.
* Dockerize FastAPI with `Dockerfile`.
* Add PostgreSQL in `docker-compose.yml`.
* Run full stack with one command:

  ```bash
  docker-compose up -d
  ```

---
