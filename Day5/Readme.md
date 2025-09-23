

# 🚀 Docker Day 5 – Ports & Volumes

### 🔹 **1. Ports (Networking)**

By default, apps running inside a container are **isolated** — the outside world can’t access them.
To expose them, we use **port mapping**:

```bash
docker run -p 8000:8000 myapp
```

👉 Explanation:

* `8000:8000` → **host\_port\:container\_port**
* First `8000` = port on your computer (host).
* Second `8000` = port inside the container where the app is running.

✅ Example: If you run a FastAPI app inside Docker on port 8000, you’ll access it in your browser at
`http://localhost:8000`

---

### 🔹 **2. Volumes (Data Persistence)**

Containers are **temporary** — when they stop, data inside them is lost.
To keep data, we use **volumes** to map local folders/files into the container.

```bash
docker run -v $(pwd):/app myapp
```

👉 Explanation:

* `-v` = volume flag
* `$(pwd)` = your current folder on the host (Windows PowerShell = `${PWD}`)
* `/app` = folder inside the container

✅ Effect: Any changes you make in your local project folder will instantly reflect inside the container.

---

### 🔹 **3. Named Volumes**

For persistent storage managed by Docker:

```bash
docker volume create mydata
docker run -v mydata:/app/data myapp
```

* `mydata` = named volume managed by Docker
* `/app/data` = path inside container

Data will survive even if the container is deleted.

---

### 📝 Day 5 Task

1. Create a small FastAPI or Flask app (on port 8000).
2. Run it with **port mapping**:

   ```bash
   docker run -p 8000:8000 myapp
   ```

   Open `http://localhost:8000` in your browser.
3. Add a file in your local project folder and mount it with:

   ```bash
   docker run -v ${PWD}:/app myapp
   ```

   Inside the container, check `/app` to see your file.

---

 