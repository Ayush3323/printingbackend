# Beginner's Guide to Dockerizing Your Project

Hello! This guide is designed to help you understand what has been done and how to run your newly "Dockerized" project.

## 1. What is Docker?

Imagine you want to ship a house to a friend. Instead of sending the bricks, wood, and furniture separately and hoping your friend knows how to assemble them exactly like you did, you put the **entire finished house** inside a giant shipping container. Your friend receives the container, opens it, and the house is there, ready to live in.

**Docker** does this for code.
- **Image**: The "blueprint" of your house. It lists everything your app needs (Python, Node.js, libraries, code).
- **Container**: The actual "house" built from the blueprint. It runs your app in an isolated environment that is *guaranteed* to look exactly like yours, no matter what computer it runs on.
- **Docker Compose**: The "city planner". It manages multiple containers (Frontend, Backend, Database) and connects them together.

## 2. What I Created for You

I added a few special files to your project:

### 1. `Dockerfile` (in `backend/`, `frontend_/`, `admin/`)
These are the blueprints.
- **Backend**: "Start with Python, install my requirements, and run the Django server."
- **Frontend/Admin**: "Start with Node.js, install my packages, and run the development server."

### 2. `docker-compose.yml` (in the root folder)
This is the master plan. It tells Docker:
- "Spin up a **Postgres** database."
- "Build and run the **Backend**, and connect it to the database."
- "Build and run the **Frontend** and **Admin** panels."

### 3. `entrypoint.sh` (in `backend/`)
This is a small helper script. It tells the backend: "Wait until the Database is fully awake before you try to connect." This prevents errors when starting up.

## 3. How to Run Your Project

### Prerequisites
You need to install **Docker Desktop** on your computer.
1. Download it from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Install it and start it.

### Commands

1. **Open your terminal** (Command Prompt or PowerShell) and navigate to your project folder:
   ```bash
   cd c:\Users\HP\Desktop\vistaprint
   ```

2. **Start everything**:
   Run this single command. It will download everything it needs, build your project, and start all services.
   ```bash
   docker-compose up --build
   ```
   *Note: The first time you run this, it might take a few minutes to download the images.*

3. **Access your apps**:
   - **Frontend**: [http://localhost:5173](http://localhost:5173)
   - **Admin Panel**: [http://localhost:5174](http://localhost:5174)
   - **Backend API**: [http://localhost:8000](http://localhost:8000)

4. **Stop everything**:
   Press `Ctrl + C` in the terminal to stop.
   To remove the containers (clean up), run:
   ```bash
   docker-compose down
   ```

## 4. Why is this better?
- **No Installation Hell**: You don't need to manually install Postgres, Redis, or specific Python versions on a new computer. You just need Docker.
- **Consistency**: The database version is locked in. Everyone working on this project sees the exact same setup.
- **Isolation**: Your project's database won't interfere with other projects on your computer.

## 5. Development Tips
I have set this up in **Development Mode**.
- **Live Reloading**: If you edit a file in your code (e.g., change a React component or a Django view), the container will detect the change and update automatically, just like before!

## 6. Troubleshooting
- **"Port already in use"**: If you see this, it means you might have another server running (like your existing `python manage.py runserver`). Make sure to stop all your old terminals before running `docker-compose up`.
- **Database data**: Docker creates a "volume" (`postgres_data`) to save your database data. Even if you restart containers, your data persists. If you want to **wipe** the database and start fresh, run:
  ```bash
  docker-compose down -v
  ```
  (The `-v` flag deletes the volumes).

## 7. Where is my old data?
You might notice that your products and users are missing. **This is normal!**

When you run `docker-compose`, it creates a **brand new, empty database** inside a container. It does *not* touch your old Postgres database installed on your Windows machine. This is good because it keeps your Docker environment clean and isolated.

### How to move your old data to Docker (Optional)
If you want to copy your data from your local computer to the Docker container, follow these steps:

1.  **Dump your local database** (Run this in a normal terminal, not Docker):
    ```bash
    pg_dump -U postgres -h localhost -p 5432 -d vistaprint_db -f local_data.sql
    ```
    *Note: We use `-f local_data.sql` instead of `> local_data.sql` to ensure the file helper saves it in the correct format (UTF-8).*

2.  **Copy the file to the Docker container**:
    ```bash
    docker-compose cp local_data.sql db:/local_data.sql
    ```

3.  **Import the data inside Docker**:
    ```bash
    docker-compose exec -T db psql -U postgres -d vistaprint_db -f /local_data.sql
    ```
    **For PowerShell Users:**
    The `<` operator doesn't work in PowerShell. Use this command instead:
    ```powershell
    cmd /c "docker-compose exec -T db psql -U postgres -d vistaprint_db < my_data.sql"
    ```
    *Note: You might see errors if tables already exist. You can ignore them or wipe the docker db first.*

Now your Docker app will have all your old data!

