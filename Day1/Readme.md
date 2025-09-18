# 🚀 Docker Day 1 – Setup & First Container

### ✅ Step 1: Install Docker

* **Windows/Mac** → [Download Docker Desktop](https://www.docker.com/products/docker-desktop)
* **Linux** → Install with:

  ```bash
  sudo apt update
  sudo apt install docker.io -y
  sudo systemctl start docker
  sudo systemctl enable docker
  ```

Check version:

```bash
docker --version
```

---

### ✅ Step 2: Run First Container

Run the hello-world container (Docker ka test image):

```bash
docker run hello-world
```

👉 Agar ye "Hello from Docker!" print kare, matlab setup ✅

---

### ✅ Step 3: Explore Containers

* Running containers check:

  ```bash
  docker ps
  ```
* Sab containers (stopped + running):

  ```bash
  docker ps -a
  ```
* Container stop/start/remove:

  ```bash
  docker stop <container_id>
  docker start <container_id>
  docker rm <container_id>
  ```

---

### 📝 Day 1 Task

1. Docker install kar ke `docker run hello-world` execute kar.
2. Ek aur container chala:

   ```bash
   docker run ubuntu echo "Docker zindabad 🚀"
   ```
3. `docker ps -a` chala ke dekh kitne containers ban gaye.

---
