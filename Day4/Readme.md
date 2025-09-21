# 🚀 Docker Day 4 – Dockerfile

### 🔹 What is a Dockerfile?

* A **Dockerfile** is a text file with instructions on how to build a Docker image.
* Think of it like a **recipe**: step-by-step instructions for creating your custom environment.
* You run `docker build` on it → Docker generates an image → then you can `docker run` it.

---

### ✅ Step 1: Basic Dockerfile Example

Create a file called **`Dockerfile`** (no extension).
Example for a simple Python app:

```dockerfile
# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files from local folder into container
COPY . .

# Run command when container starts
CMD ["python", "app.py"]
```

---

### ✅ Step 2: Build an Image

Build the Dockerfile into an image:

```bash
docker build -t myapp .
```

* `-t myapp` = name (tag) for your image.
* `.` = current directory (where Dockerfile is).

---

### ✅ Step 3: Run Your Container

Run your image:

```bash
docker run myapp
```

If your `app.py` has:

```python
print("Hello from Docker 🚀")
```

The container will print that when it runs.

---

### ✅ Step 4: More Useful Instructions

1. **Installing dependencies (requirements.txt)**

   ```dockerfile
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   ```
2. **Expose ports**

   ```dockerfile
   EXPOSE 8000
   ```
3. **Environment variables**

   ```dockerfile
   ENV NAME=Maroof
   ```

---

### 📝 Day 4 Task

1. Create a folder `Day4/` with a file `app.py`:

   ```python
   print("Dockerfile Day 4 ✅")
   ```
2. Write a `Dockerfile` (like above).
3. Build the image:

   ```bash
   docker build -t day4app .
   ```
4. Run the container:

   ```bash
   docker run day4app
   ```

---
