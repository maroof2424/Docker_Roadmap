# 🚀 Docker Day 2 – Images

### 🔹 What is a Docker Image?

* An **image** is like a **template / blueprint** for creating containers.
* Example: `python:3.10` image → lets you spin up a container that already has Python 3.10 installed.
* **Container = Running instance of an image.**

---

### ✅ Step 1: Pull Images

Download images from Docker Hub (the public registry):

```bash
docker pull ubuntu
docker pull python:3.10
```

---

### ✅ Step 2: List Images

Check what images you have:

```bash
docker images
```

You’ll see columns like:

* **REPOSITORY** (name, e.g., `python`)
* **TAG** (version, e.g., `3.10`)
* **IMAGE ID**
* **SIZE**

---

### ✅ Step 3: Remove Images

If you want to remove an image:

```bash
docker rmi <image_id_or_name>
```

Remove all unused images:

```bash
docker image prune
```

---

### ✅ Step 4: Run Containers from Images

Run Python interactively inside a container:

```bash
docker run -it python:3.10 python
```

👉 This drops you into a Python REPL (inside container). Try:

```python
print("Hello from inside Docker!")
```

Exit with `exit()` or `Ctrl+D`.

---

### ✅ Step 5: Inspect Images

Check details about an image:

```bash
docker inspect python:3.10
```

---

### 📝 Day 2 Task

1. Pull `ubuntu` and `python:3.10` images.
2. Run `docker images` and confirm both are there.
3. Run Python in a container and print `"Docker Day 2 ✅"`.
4. Remove the `ubuntu` image using `docker rmi`.
5. Try `docker image prune` to clean unused images.

---

