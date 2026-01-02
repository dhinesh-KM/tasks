Django REST API – Users & Tasks (Dockerized Development Setup)

This project is a simple Django REST API for managing Users and Tasks, built using Django, Django REST Framework, and PostgreSQL, fully containerized with Docker for development.

🚀 Tech Stack

Python 3.11

Django 4.x

Django REST Framework (DRF)

PostgreSQL 15

Docker & Docker Compose

⚙️ Setup Instructions
🐳 Option 1: Dockerized Development Setup (Recommended)
1️⃣ Prerequisites

    Docker
    
    Docker Compose
  
2️⃣ Clone the Repository
      git clone https://github.com/dhinesh-KM/tasks.git
      cd task_manager

3️⃣ Environment Variables

  Create a .env file in the root directory:

    POSTGRES_DB=taskdb
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

4️⃣ Build and Start Containers

  docker-compose up --build
  
    Django API → http://localhost:8000

    Django Admin → http://localhost:8000/admin

🐘 PostgreSQL Configuration

PostgreSQL runs as a separate Docker service.

Connection details (used internally by Django):

  Host: db
  
  Port: 5432
  
  Database: taskdb
  
  Username: postgres
  
  Password: postgres
  
Database data is persisted using Docker volumes.


🧩 Migration Commands

  Run migrations in a separate terminal while containers are running:
  
    # Create migration files (when models change)
      docker-compose exec task python app/manage.py makemigrations
    
    
    # Apply migrations to database
      docker-compose exec task python app/manage.py migrate
  
    # Create a superuser for Django Admin:
      docker-compose exec task python app/manage.py createsuperuser

💻 Option 2: Local Development Setup (Without Docker)
1️⃣ Prerequisites

    Python 3.11
    
    PostgreSQL 15
    
    pip
    
    virtualenv (recommended)
2️⃣ Clone the Repository
      git clone https://github.com/dhinesh-KM/tasks.git
      cd task_manager
      
  3️⃣ Create & Activate Virtual Environment
      python -m venv venv
      
      
      Windows
      
        venv\Scripts\activate
      
      
      Linux / macOS
      
        source venv/bin/activate
  
  4️⃣ Install Dependencies
      pip install -r requirements.txt
  
  5️⃣ PostgreSQL Setup (Local)
  
      Create a PostgreSQL database:
      
      CREATE DATABASE taskdb;
  
  6️⃣ Environment Variables (Local)
  
    Create a .env file in the root directory:
  
      POSTGRES_DB=taskdb
      POSTGRES_USER=postgres
      POSTGRES_PASSWORD=postgres
      POSTGRES_HOST=localhost
      POSTGRES_PORT=5432
    
    
  7️⃣ Run Migrations
      python app/manage.py makemigrations
      python app/manage.py migrate
  
  8️⃣ Create Superuser
      python app/manage.py createsuperuser
  
  9️⃣ Start Development Server
      python app/manage.py runserver

🛠 Admin Panel

  URL: http://localhost:8000/admin
  
  Allows managing users and tasks via UI

🔗 API Documentation
    This project includes a Swagger (OpenAPI) specification for the API.
    
    The file is located at:
    
    task_manager/swagger_specs.yaml



🔌 API Endpoints
  👤 Users
  
    POST /api/v1/users/ – Create a new user
    
    GET /api/v1/users/ – List all users
  
  📝 Tasks
  
    POST /api/v1/tasks/ – Create a new task
    
    GET /api/v1/tasks/ – List all tasks
    
    GET /api/v1/tasks/{id}/ – Retrieve task details
    
    PUT /api/v1/tasks/{id}/ – Update a task
    
    DELETE /api/v1/tasks/{id}/ – Delete a task

  🔍 Filtering

  GET /api/v1/tasks/?status=Completed – Filter tasks by status
  
  Supported values:
  
    Pending
    
    In Progress
    
    Completed
            
