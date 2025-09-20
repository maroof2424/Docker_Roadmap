

# ⚡ Docker Day 3 – Container Lifecycle

### 🔹 Container Lifecycle Stages

1. **Created** → when a container is made from an image.
2. **Running** → when it’s actively working.
3. **Paused/Stopped (Exited)** → container finished its task or was stopped.
4. **Removed** → deleted completely.

---

### ✅ Step 1: Create & Run Container

Run a container (Ubuntu):

```bash
docker run -it ubuntu bash
```

* `-it` = interactive + terminal.
* Inside container, try:

  ```bash
  ls
  pwd
  echo "Hello from inside container"
  ```
* Exit with `exit`.

---

### ✅ Step 2: List Containers

* Running containers:

  ```bash
  docker ps
  ```
* All containers (including stopped):

  ```bash
  docker ps -a
  ```

---

### ✅ Step 3: Start / Stop / Restart Containers

* Start an existing container:

  ```bash
  docker start <container_id_or_name>
  ```
* Stop a running container:

  ```bash
  docker stop <container_id_or_name>
  ```
* Restart container:

  ```bash
  docker restart <container_id_or_name>
  ```

---

### ✅ Step 4: Attach & Exec

* Attach back to a running container:

  ```bash
  docker attach <container_id>
  ```
* Run a command in an existing container:

  ```bash
  docker exec -it <container_id> bash
  ```

---

### ✅ Step 5: Remove Containers

* Remove single container:

  ```bash
  docker rm <container_id_or_name>
  ```
* Remove all stopped containers:

  ```bash
  docker container prune
  ```

---

### 📝 Day 3 Task

1. Run `docker run -it ubuntu bash`, explore inside, then exit.
2. Check it in `docker ps -a`.
3. Restart the same container using `docker start <id>`.
4. Use `docker exec -it <id> bash` to re-enter.
5. Remove the container with `docker rm <id>`.

---

